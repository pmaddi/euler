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
        return this.highCard().value();
    }
    return cmp;
}

Hand.prototype.highCard = function() {
    const idx = argMax(this.cards.map(c => c.value()));
    return this.cards[idx];
}


function compare(h1, h2) {
    h1.flush() && (h1.straight() == 14)


}

function main() {
    fs.readFile('p054_poker.txt', 'utf8', function(err, data) {
        const lines = data.split('\n');
        const hand_arrs = lines.map(ln => ln.split(' '))
        const hands = hand_arrs.map(
            cd_strs => [new Hand(cd_strs.slice(5)), 
                        new Hand(cd_strs.slice(5, 10))])

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

    main();
}
