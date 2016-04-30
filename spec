var fb = require('../fizzbuzz');

describe("A program that plays fizzbuzz", function() {

	it("can count from 1 to 6 and make appropirate substitutions", function() {
	expect(fb.count(1,6)).toBe("1 2 fizz 4 buzz fizz");
	expect(fb.count(11,15)).toBe("11 fizz 13 14 fizzbuzz");
	});


	it("can take multiples of 3 and return 'fizz' and the number otherwise", function() {
		expect(fb.fizzer(3)).toBe('fizz');
		expect(fb.fizzer(33)).toBe('fizz');
		expect(fb.fizzer(81)).toBe('fizz');
	});

	it("can take multiples of 5 and return 'buzz' and the number otherwise", function() {
		expect(fb.buzzer(5)).toBe('buzz');
		expect(fb.buzzer(6)).toBe('6');
		expect(fb.buzzer(17)).toBe('17');
	});

	it("can take multiples of 3 and 5 and return 'fizzbuzz' and the number otherwise", function() {
		expect(fb.fizzbuzzer(15)).toBe('fizzbuzz');
		expect(fb.fizzbuzzer(6)).toBe('6');
		expect(fb.fizzbuzzer(17)).toBe('17');
	});
});
