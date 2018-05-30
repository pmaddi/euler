// Fails because the ints overflow. :(

var Fraction = require('fractional').Fraction

function digit_count(it) {
    return it.toString().length;
}

var TBL = {};
function next(f) {
    if (f.toString() in TBL) {
        return TBL[f.toString()];
    }
    var new_f = (new Fraction(2)).add((new Fraction(1)).divide(f));
    TBL[f.toString()] = new_f;
    return new_f;
}

if (typeof require != 'undefined' && require.main==module) {
    var f = (new Fraction(2.0));
    const arr = new Array();

    var count = 0;
    for (var i=1; i < 1001; i ++) {
        const val = ((new Fraction(1)).add((new Fraction(1)).divide(f)));
        if (digit_count(val.numerator) > digit_count(val.denominator)) {
            count ++;
        }
        console.log(count, i);
        arr.push(val);
        f = next(f);
    }

    console.log(arr);
}
