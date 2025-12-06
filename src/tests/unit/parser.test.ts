import { parsePrompt } from '../../utils/parser';

describe('Smart Variable Engine - Parser', () => {
  test('should extract simple variables', () => {
    const prompt = 'Hello {{Name}}, welcome to {{Place}}.';
    const variables = parsePrompt(prompt);

    expect(variables).toHaveLength(2);
    expect(variables[0].name).toBe('Name');
    expect(variables[0].type).toBe('text');
    expect(variables[1].name).toBe('Place');
    expect(variables[1].type).toBe('text');
  });

  test('should extract select variables', () => {
    const prompt = 'Write a {{Tone:Professional|Casual}} email.';
    const variables = parsePrompt(prompt);

    expect(variables).toHaveLength(1);
    expect(variables[0].name).toBe('Tone');
    expect(variables[0].type).toBe('select');
    expect(variables[0].options).toEqual(['Professional', 'Casual']);
    expect(variables[0].defaultValue).toBe('Professional');
  });

  test('should extract number variables', () => {
    const prompt = 'Max length: {{Length#100}}.';
    const variables = parsePrompt(prompt);

    expect(variables).toHaveLength(1);
    expect(variables[0].name).toBe('Length');
    expect(variables[0].type).toBe('number');
    expect(variables[0].defaultValue).toBe('100');
  });

  test('should deduplicate variables', () => {
    const prompt = '{{Topic}} is a great topic. I love {{Topic}}.';
    const variables = parsePrompt(prompt);

    expect(variables).toHaveLength(1);
    expect(variables[0].name).toBe('Topic');
  });
});
