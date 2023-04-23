function randomizeStyles(answerSide) {
    let single = globalThis.RSingleStyles;
    let multi = globalThis.RMultiStyles;
    if (globalThis.RCardStyles !== undefined) {
        single = globalThis.RCardStyles.single;
        multi = globalThis.RCardStyles.multi;
    } else {
        globalThis.RCardStyles = { single: {}, multi: [] };
    }

    function randItem(array) {
        return array[Math.floor(Math.random() * array.length)];
    }

    for (const propertyName of Object.keys(single)) {
        const value = randItem(single[propertyName]);
        globalThis.RCardStyles.single[propertyName] = [value];
        document.body.style[propertyName] = value;
    }
    const randComb = randItem(multi);
    globalThis.RCardStyles.multi.push(randComb);
    for (const propertyName of Object.keys(randComb)) {
        document.body.style[propertyName] = randComb[propertyName];
    }

    if (answerSide) {
        globalThis.RCardStyles = undefined;
    }
}
