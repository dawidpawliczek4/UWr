let obj = {
    name: 'dawid',
    method() {
        return this.name + 'dawid'
    },
    get test() {
        return this.name
    },
    set test(newVal) {
        this.name = newVal
    }
}

Object.defineProperty(obj, 'nowePole', {
    value: 42,
    writable: true, // Możliwe do modyfikacji
    enumerable: true, // Widoczne w iteracjach
    configurable: true // Można usunąć to pole
});
Object.defineProperty(obj, 'nowaMetoda', {
    value: function() {
        return this.nowePole * 3;
    },
    writable: true,
    enumerable: true,
    configurable: true
});
Object.defineProperty(obj, 'nowaWartosc', {
    get: function() {
        return this.nowePole;
    },
    set: function(nowaWartosc) {
        this.nowePole = nowaWartosc;
    },
    enumerable: true,
    configurable: true
});


/**
Pole może być dodane bezpośrednio lub za pomocą Object.defineProperty. Jednak, aby mieć pełną kontrolę nad właściwościami takimi jak writable, enumerable, czy configurable, musi być użyty Object.defineProperty.

Metoda może być dodana bezpośrednio jako funkcja lub za pomocą Object.defineProperty. Podobnie jak w przypadku pól, aby mieć pełną kontrolę nad konfiguracją, musi być użyty Object.defineProperty.

Właściwości z akcesorami (tj. get i set) muszą być dodane przy pomocy Object.defineProperty, ponieważ bez tego nie można bezpośrednio określić funkcji get i set przy definiowaniu nowych właściwości na istniejących obiektach.
 */