fs = require('fs');
// Warn if overriding existing method
if(Array.prototype.equals)
    console.warn("Overriding existing Array.prototype.equals. Possible causes: New API defines the method, there's a framework conflict or you've got double inclusions in your code.");
// attach the .equals method to Array's prototype to call it on any array
Array.prototype.equals = function (array) {
    // if the other array is a falsy value, return
    if (!array)
        return false;

    // compare lengths - can save a lot of time 
    if (this.length != array.length)
        return false;

    for (var i = 0, l=this.length; i < l; i++) {
        // Check if we have nested arrays
        if (this[i] instanceof Array && array[i] instanceof Array) {
            // recurse into the nested arrays
            if (!this[i].equals(array[i]))
                return false;       
        }           
        else if (this[i] != array[i]) { 
            // Warning - two different object instances will never be equal: {x:20} != {x:20}
            return false;   
        }           
    }       
    return true;
}
// Hide method from for-in loops
Object.defineProperty(Array.prototype, "equals", {enumerable: false});
function argMax(array) {
    return array.map((x, i) => [x, i]).reduce((r, a) => (a[0] > r[0] ? a : r))[1];
}
function assert(condition, message) {
    if (!condition) {
        message = message || "Assertion failed";
        if (typeof Error !== "undefined") {
            throw new Error(message);
        }
        throw message; // Fallback
    }
}

function Card(st) {
    this.hand_string = st;
}
Card.prototype.suit = function() {
    return this.hand_string.charAt(1);
}
Card.prototype.value = function() {
    const lookup = {
        A: 14,
        K: 13,
        Q: 12,
        J: 11,
        T: 10,
    };
    const c = this.hand_string.charAt(0);
    if (c in lookup) {
        return lookup[c];
    } else {
        return Number(c);
    }
}

function Hand(card_str_array) {
    const cards = card_str_array.map(s => new Card(s));
    this.cards = cards;
}
Hand.prototype.handSize = function()  {
    return this.cards.length;
}

function counts(arr) {
    return arr.reduce((agg, val) => {
        if (val in agg) {
            agg[val] = agg[val] + 1;
        } else {
            agg[val] = 1;
        }
        return agg;
    }, {});
}
Hand.prototype.threeOfAKind = function() {
    if (this.cards.length < 3) {
        return false;
    }
    const cnts = counts(this.cards.map(c => c.value()));
    var msf_k = 0;
    Object.entries(cnts).forEach(([k, v]) => {
        const key = Number(k);
        if (v >= 3) {
            if (key > msf_k) {
                msf_k = key;
            }
        };
    });
    return msf_k;
}
Hand.prototype.fourOfAKind = function() {
    if (this.cards.length < 4) {
        return false;
    }
    const cnts = counts(this.cards.map(c => c.value()));
    var msf_k = 0;
    Object.entries(cnts).forEach(([k, v]) => {
        const key = Number(k);
        if (v >= 4) {
            if (key > msf_k) {
                msf_k = key;
            }
        };
    });
    return msf_k;
}
Hand.prototype.twoOfAKind = function() {
    if (this.cards.length < 2) {
        return false;
    }
    const cnts = counts(this.cards.map(c => c.value()));
    var msf_k = 0;
    Object.entries(cnts).forEach(([k, v]) => {
        const key = Number(k);
        if (v >= 2) {
            if (key > msf_k) {
                msf_k = key;
            }
        };
    });
    return msf_k;
}
Hand.prototype.fullHouse = function() {
    if (this.cards.length < 5) {
        return false;
    }
    const threeK = this.threeOfAKind();
    if (!threeK) {
        return false;
    }
    const remaining = this.cards.filter(c => c.value() !== threeK);
    const remHand = new Hand(remaining.map(c => c.hand_string));
    const twoK = remHand.twoOfAKind();
    if (!twoK) {
        return false;
    }
    return [threeK, twoK];

}
Hand.prototype.twoPair = function() {
    if (this.cards.length < 4) {
        return false;
    }
    const twoK1 = this.twoOfAKind();
    if (!twoK1) {
        return false;
    }
    const remaining = this.cards.filter(c => c.value() !== twoK1);
    const remHand = new Hand(remaining.map(c => c.hand_string));
    const twoK2 = remHand.twoOfAKind();
    if (!twoK2) {
        return false;
    }
    return [twoK1, twoK2];

}
Hand.prototype.straight = function() {
    if (this.cards.length !== 5) {
        return false;
    }
    const vals = this.cards.map(c => c.value());
    const sorted_vals = vals.sort();
    const mn = Math.min(...sorted_vals);

    var i = 0;
    while (i < sorted_vals.length) {
        if (!(sorted_vals[i] === mn + i)) {
            return false;
        }
        i ++;
    }
    return Math.max(...sorted_vals);
}

Hand.prototype.flush = function() {
    if (this.cards.length !== 5) {
        return false;
    }
    const cmp = this.cards.reduce((agg, val) => {
        if (agg === null) {
            return val.suit()
        } else if (!agg) {
            return agg
        } else {
            if (val.suit() === agg) {
                return agg
            } else {
                return false
            }
        }
    }, null);
    if (cmp) {
        return this.highCard();
    }
    return cmp;
}

Hand.prototype.highCard = function() {
    if (this.cards.length < 1) {
        return false;
    }
    const idx = argMax(this.cards.map(c => c.value()));
    return this.cards[idx].value();
}

Hand.prototype.royalFlush = function () {
    return this.flush() && (this.straight() == 14)
}

Hand.prototype.straightFlush = function () {
    if (this.flush() && this.straight()) {
        return this.straight();
    }
    return false;
}

Hand.prototype.cardsString = function () {
    return this.cards.map(c => c.hand_string).join(' ');
}

function maxof(h1, h2) {
    if (h1 > h2) {
        return -1;
    } else if (h2 > h1) {
        return 1;
    }
    return 0;
}
function listMaxOf(h1, h2) {
    if (h1[0] > h2[0]) {
        return -1;
    } else if (h2[0] > h1[0]) {
        return 1;
    } else if (h1[1] > h2[1]) {
        return -1;
    } else if (h2[1] > h1[1]) {
        return 1;
    }
    return 0;
}

function compare(h1, h2) {
    // Returns -1 0 or 1. -1 means h1 won , 0 means tie and 1 means h2 won.
    if (h1.royalFlush() && h2.royalFlush()) {
        return 0;
    } else if (h1.royalFlush()) {
        return -1;
    } else if (h2.royalFlush()) {
        return 1;
    }
    if (h1.straightFlush() && h2.straightFlush()) {
        return maxof(h1.straightFlush(), h2.straightFlush());
    } else if (h1.straightFlush()) {
        return -1;
    } else if (h2.straightFlush()) {
        return 1;
    }
    if (h1.fourOfAKind() && h2.fourOfAKind()) {
        return maxof(h1.fourOfAKind(), h2.fourOfAKind());
    } else if (h1.fourOfAKind()) {
        return -1;
    } else if (h2.fourOfAKind()) {
        return 1;
    }
    if (h1.fullHouse() && h2.fullHouse()) {
        return listMaxOf(h1.fullHouse(), h2.fullHouse());
    } else if (h1.fullHouse()) {
        return -1;
    } else if (h2.fullHouse()) {
        return 1;
    }
    if (h1.flush() && h2.flush()) {
        return maxof(h1.flush(), h2.flush());
    } else if (h1.flush()) {
        return -1;
    } else if (h2.flush()) {
        return 1;
    }
    if (h1.straight() && h2.straight()) {
        return maxof(h1.straight(), h2.straight());
    } else if (h1.straight()) {
        return -1;
    } else if (h2.straight()) {
        return 1;
    }
    if (h1.threeOfAKind() && h2.threeOfAKind()) {
        const m = maxof(h1.threeOfAKind(), h2.threeOfAKind());
        if (m) {
            return m;
        } else {
            const threeVal = h1.threeOfAKind();
            const newh1 = new Hand(h1.cards
                .filter(c => c.value() !== threeVal)
                .map(c => c.hand_string));
            const newh2 = new Hand(h2.cards
                .filter(c => c.value() !== threeVal)
                .map(c => c.hand_string));
            return compare(newh1, newh2);
        }
    } else if (h1.threeOfAKind()) {
        return -1;
    } else if (h2.threeOfAKind()) {
        return 1;
    }
    if (h1.twoPair() && h2.twoPair()) {
        const m = listMaxOf(h1.twoPair(), h2.twoPair());
        if (m) {
            return m;
        } else {
            const [twoOne, twoTwo] = h1.twoPair();
            const newh1 = new Hand(h1.cards
                .filter(c => (c.value() !== twoOne) && (c.value() !== twoTwo))
                .map(c => c.hand_string));
            const newh2 = new Hand(h2.cards
                .filter(c => (c.value() !== twoOne) && (c.value() !== twoTwo))
                .map(c => c.hand_string));
            return compare(newh1, newh2);
        }
    } else if (h1.twoPair()) {
        return -1;
    } else if (h2.twoPair()) {
        return 1;
    }
    if (h1.twoOfAKind() && h2.twoOfAKind()) {
        const m = maxof(h1.twoOfAKind(), h2.twoOfAKind());
        if (m) {
            return m;
        } else {
            const twoKind = h1.twoOfAKind();
            const newh1 = new Hand(h1.cards
                .filter(c => c.value() !== twoKind)
                .map(c => c.hand_string));
            const newh2 = new Hand(h2.cards
                .filter(c => c.value() !== twoKind)
                .map(c => c.hand_string));
            return compare(newh1, newh2);
        }
    } else if (h1.twoOfAKind()) {
        return -1;
    } else if (h2.twoOfAKind()) {
        return 1;
    }
    if (h1.highCard() && h2.highCard()) {
        const m = maxof(h1.highCard(), h2.highCard());
        if (m) {
            return m;
        } else {
            const highCard = h1.highCard();
            const newh1 = new Hand(h1.cards
                .filter(c => c.value() !== highCard)
                .map(c => c.hand_string));
            const newh2 = new Hand(h2.cards
                .filter(c => c.value() !== highCard)
                .map(c => c.hand_string));
            
            // console.log(`${highCard} ${h1.cardsString()} ${h2.cardsString()} rec4`);
            return compare(newh1, newh2);
        }
    } else if (h1.highCard()) {
        return -1;
    } else if (h2.highCard()) {
        return 1;
    }
    return 0;
}

function results(fname, cb) {
    fs.readFile(fname, 'utf8', function(err, data) {
        const lines = data.split('\n').filter(l => l !== '');
        const hand_arrs = lines.map(ln => ln.split(' '))
        const hands = hand_arrs.map(
            cd_strs => [new Hand(cd_strs.slice(0, 5)), 
                        new Hand(cd_strs.slice(5, 10))]);
        // console.log(hands.slice(2));
        const handResults = hands.map(hs => {
            // console.log(hs[0]);
            // console.log(hs[1]);
            // console.log('***');
            const cmp = compare(hs[0], hs[1]);
            if (cmp === 0) {
                console.log(hs[0], hs[1]);
            }
            return cmp;
        });
        cb(handResults);
    });
}

function main() {
    results('p054_poker.txt', r => {
        console.log(counts(r)[-1]);
    });
}

if (typeof require != 'undefined' && require.main==module) {
    const cd = new Card('2D');
    assert(cd.suit() === 'D');
    assert(cd.value() === 2);
    const cd1 = new Card('KD');
    assert(cd1.value() === 13);

    const hd1 = new Hand(['2D','3D', '4D', '5D','6D'])
    assert(hd1.flush() === 6);
    assert(hd1.straight() === 6);
    const hd2 = new Hand(['2S','3D', '4D', '5D','7D'])
    assert(!hd2.flush());
    assert(!hd2.straight());
    assert(!hd2.threeOfAKind());

    const hd3 = new Hand(['2S','2D', '2C', '5D','7D'])
    assert(hd3.threeOfAKind() === 2);
    assert(!hd3.fourOfAKind());

    const hd4 = new Hand(['2S','2D', '2C', '2N','7D'])
    assert(hd4.fourOfAKind() === 2);
    assert(!hd4.fullHouse());

    const hd5 = new Hand(['2S','2D', '3C', '3N','7D'])
    assert(hd5.twoOfAKind() === 3);
    assert(!hd5.fullHouse());

    const hd6 = new Hand(['2S', '2D', '2X', '5N', '5S']);
    assert(hd6.fullHouse().equals([2, 5]));

    const hd7 = new Hand(['2S', '2D', '2X', '5N', '5S']);
    assert(hd6.twoPair().equals([5, 2]));

    assert(hd6.highCard() === 5);
    assert(hd5.highCard() === 7);

    assert(compare(hd6, hd7) === 0);
    assert(compare(hd4, hd6) === -1);
    assert(compare(hd5, hd6) === 1);

    assert(compare(new Hand(['5H', '5C', '6S', '7S', 'KD']),
                   new Hand(['2C', '3S', '8S', '8D', 'TD'])) === 1);
    results('p054_poker_test.txt', r => {
        assert(r.equals([1, -1, 1, -1, -1]));
    });

    main();
}
