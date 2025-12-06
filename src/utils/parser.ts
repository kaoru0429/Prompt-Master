export interface Variable {
    name: string;
    type: 'text' | 'select' | 'number';
    options?: string[];
    defaultValue?: string;
    value: string;
}

export function parsePrompt(inputPrompt: string) {
    const regex = /\{\{(.*?)\}\}/g;
    const matches = Array.from(inputPrompt.matchAll(regex));

    const newVariables: Variable[] = matches.map((match) => {
      const content = match[1];
      let name = content;
      let type: Variable['type'] = 'text';
      let options: string[] | undefined;
      let defaultValue: string | undefined;

      // Check for Select type (e.g., Tone:Professional|Casual)
      if (content.includes(':')) {
        const parts = content.split(':');
        name = parts[0];
        type = 'select';
        options = parts[1].split('|');
        defaultValue = options[0];
      }
      // Check for Number type (e.g., WordCount#1000)
      else if (content.includes('#')) {
        const parts = content.split('#');
        name = parts[0];
        type = 'number';
        defaultValue = parts[1];
      }

      return {
        name,
        type,
        options,
        defaultValue,
        value: defaultValue || '',
      };
    });

    // Deduplicate variables by name
    const uniqueVariables = newVariables.reduce((acc, current) => {
      const x = acc.find(item => item.name === current.name);
      if (!x) {
        return acc.concat([current]);
      } else {
        return acc;
      }
    }, [] as Variable[]);

    return uniqueVariables;
}
