function assert(condition, message) {
    if (!condition) {
        message = message || "Assertion failed";
        if (typeof Error !== "undefined") {
            throw new Error(message);
        }
        throw message; // Fallback
    }
}

function reverse(n) {
    const digs = Math.floor(Math.log10(n)) + 1;
    var out = 0;
    for (var i = 0; i < digs; i++) {
        const v = Math.pow(10, i);
        const o = Math.floor(n / v) % 10;
        out = out * 10 + o;
    }
    return out;
}

function isPalindrome(n) {
    return reverse(n) === n
}

function isPalindromeInLtKIterations(n, k) {
    // Returns false if cannot be done and the number of iterations (greater
    // than 0) otherwise 
    var next = n;
    for (var it = 1; it <= k; it ++) {
        next = reverse(next) + next;
        if (isPalindrome(next)) {
            return it;
        }
    }
    return false;
}

function lychrelNumberCountUnderK(k) {
    var count = 0;
    for (var it = 1; it < k; it ++) {
        if (!isPalindromeInLtKIterations(it, 50)) {
            count ++;
        }
    }
    return count;
}

function main() {
    assert(reverse(1) === 1);
    assert(reverse(123) === 321);
    assert(isPalindromeInLtKIterations(47, 50) == 1);
    assert(isPalindromeInLtKIterations(349, 50) == 3);
    assert(!isPalindromeInLtKIterations(196, 50));
    console.log(lychrelNumberCountUnderK(10000));
}
main();
