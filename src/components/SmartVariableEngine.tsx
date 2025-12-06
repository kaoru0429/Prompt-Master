import React, { useState, useEffect } from 'react';
import { parsePrompt, Variable } from '@/utils/parser';

const SmartVariableEngine: React.FC = () => {
  const [title, setTitle] = useState<string>('部落格文章生成器');
  const [description, setDescription] = useState<string>('這是一個用於生成專業或輕鬆風格部落格文章的模板。');
  const [prompt, setPrompt] = useState<string>(
    'Write a {{Tone:Professional|Casual}} blog post about {{Topic}} with {{WordCount#1000}} words.'
  );
  const [variables, setVariables] = useState<Variable[]>([]);
  const [generatedPrompt, setGeneratedPrompt] = useState<string>('');

  const handleParse = (inputPrompt: string) => {
    // Preserve current values if variable name still exists
    const currentValues = variables.reduce((acc, v) => {
      acc[v.name] = v.value;
      return acc;
    }, {} as Record<string, string>);

    const newVariables = parsePrompt(inputPrompt).map(v => ({
      ...v,
      value: currentValues[v.name] || v.defaultValue || ''
    }));
    setVariables(newVariables);
  };

  // Update generated prompt when variables or prompt changes
  useEffect(() => {
    let result = prompt;
    variables.forEach((variable) => {
      const regex = /\{\{(.*?)\}\}/g;
      result = result.replace(regex, (match, content) => {
         let name = content;
         if (content.includes(':')) name = content.split(':')[0];
         else if (content.includes('#')) name = content.split('#')[0];

         const v = variables.find(v => v.name === name);
         return v ? v.value : match;
      });
    });
    setGeneratedPrompt(result);
  }, [prompt, variables]);

  const handleVariableChange = (name: string, value: string) => {
    setVariables((prev) =>
      prev.map((v) => (v.name === name ? { ...v, value } : v))
    );
  };

  // Initial parse
  useEffect(() => {
      handleParse(prompt);
      // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <div className="p-4 border rounded shadow-md bg-white max-w-4xl mx-auto">
      <h2 className="text-2xl font-bold mb-6 text-gray-800">Smart Variable Engine</h2>

      <div className="mb-6 space-y-4">
        <div>
            <label className="block text-sm font-semibold text-gray-700 mb-1">標題 (Title)</label>
            <input
                type="text"
                className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
                value={title}
                onChange={(e) => setTitle(e.target.value)}
                placeholder="輸入 Prompt 標題..."
            />
        </div>

        <div>
            <label className="block text-sm font-semibold text-gray-700 mb-1">情境說明 (Context)</label>
            <textarea
                className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
                rows={2}
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                placeholder="輸入情境說明..."
            />
        </div>

        <div>
            <label className="block text-sm font-semibold text-gray-700 mb-1">Prompt 模板</label>
            <textarea
            className="w-full p-2 border border-gray-300 rounded font-mono text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition"
            rows={4}
            value={prompt}
            onChange={(e) => {
                setPrompt(e.target.value);
            }}
            onBlur={() => handleParse(prompt)}
            />
            <p className="text-xs text-gray-500 mt-1">
                使用 <code className="bg-gray-100 px-1 rounded">{'{{Variable}}'}</code> 定義變數，
                <code className="bg-gray-100 px-1 rounded">{'{{Name:Option1|Option2}}'}</code> 定義選單，
                <code className="bg-gray-100 px-1 rounded">{'{{Name#DefaultValue}}'}</code> 定義數值。
            </p>
        </div>
      </div>

      {variables.length > 0 && (
        <div className="mb-6 p-6 bg-gray-50 rounded-lg border border-gray-200">
          <h3 className="text-lg font-bold mb-4 text-gray-700 flex items-center">
            <span className="mr-2">⚙️</span> 變數設定
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            {variables.map((variable) => (
              <div key={variable.name} className="space-y-1">
                <label className="block text-sm font-medium text-gray-700">{variable.name}</label>
                {variable.type === 'select' ? (
                  <select
                    className="w-full p-2 border border-gray-300 rounded bg-white focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
                    value={variable.value}
                    onChange={(e) => handleVariableChange(variable.name, e.target.value)}
                  >
                    {variable.options?.map((opt) => (
                      <option key={opt} value={opt}>
                        {opt}
                      </option>
                    ))}
                  </select>
                ) : variable.type === 'number' ? (
                  <input
                    type="number"
                    className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
                    value={variable.value}
                    onChange={(e) => handleVariableChange(variable.name, e.target.value)}
                  />
                ) : (
                  <input
                    type="text"
                    className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none"
                    value={variable.value}
                    onChange={(e) => handleVariableChange(variable.name, e.target.value)}
                  />
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      <div>
        <label className="block text-sm font-semibold text-gray-700 mb-1">預覽結果</label>
        <div className="w-full p-4 border border-gray-300 rounded-lg bg-gray-900 text-gray-100 min-h-[120px] whitespace-pre-wrap font-mono text-sm leading-relaxed">
          {generatedPrompt}
        </div>
      </div>
    </div>
  );
};

export default SmartVariableEngine;
