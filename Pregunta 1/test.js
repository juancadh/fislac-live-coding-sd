const chai = window.chai;
const expect = chai.expect;
const assert = chai.assert;

describe('maxSumFunction', () => {

    it('No debe permitir objetos que no sean un arreglo', () => {
        assert.throws(()=> maxSumFunction(12), TypeError)
        assert.throws(()=> maxSumFunction(12,3), TypeError)
        assert.throws(()=> maxSumFunction("w"), TypeError)
    })

    it('No debe permitir arreglos menores a 2 elementos', () => {
        assert.throws(()=> maxSumFunction([12]), TypeError)
        assert.throws(()=> maxSumFunction([]), TypeError)
    })

    it('Debe encontrar el par de valores con la suma máxima', () => {        
        expect(maxSumFunction([12, 34, 10, 31, 6, 40])).to.deep.equal(74)
        expect(maxSumFunction([4, 80, 5, 90, 50, 51, 67])).to.deep.equal(170)
        expect(maxSumFunction([4, 80, 5])).to.deep.equal(85)
        expect(maxSumFunction([12, 9, 8, 34, 8, 10, 43, 43, 2, 1])).to.deep.equal(86)
    });

})