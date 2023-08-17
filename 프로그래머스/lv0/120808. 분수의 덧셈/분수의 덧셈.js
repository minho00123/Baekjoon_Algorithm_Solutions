function solution(numer1, denom1, numer2, denom2) {
    let answer = [];
    let numer = numer1 * denom2 + numer2 * denom1;
    let denom = denom1 * denom2;
    for (let i = Math.min(numer, denom); i >= 2; i--) {
        if (numer % i === 0 && denom % i === 0) {
            numer /= i;
            denom /= i;
        }
    }
    answer.push(numer);
    answer.push(denom);
    return answer;
}