from unittest import TestCase, skip
from paramunittest import parametrized

from nlg.tools import diffFormat, skipTest, assertEqual
from nlg.surface import surfaceRealize

tests = [
    {
        'test': {},
        'data': {
            'id': 'support',
            'input': [
                {
                    'symbols': ['f'],
                    'type': 'real',
                    'kind': 'function',
                    'dependencies': ['x']
                }
            ],
            'equivalence': [
                {
                    'function': ['f'],
                    'is': ['support'],
                    'of': {
                            'symbol': 'x',
                            'from': 'a',
                            'to': 'c'
                    }
                },
                {
                    'expression': {
                            'operator': 'neq',
                            'lhs': 'f(b)',
                            'rhs': '0'
                        },
                        'forall': ['b']
                }
            ],
            'symbols': [
                {
                    'symbols': ['x'],
                    'type': 'real',
                    'kind': 'variable'
                },
                {
                    'symbols': ['a', 'b', 'c'],
                    'type': 'real',
                    'kind': 'constant',
                    'constraints': [
                        {
                            'symbol': 'b',
                            'type': 'inside',
                            'lb': 'a',
                            'ub': 'c'
                        }
                    ]
                }
            ]
        },
        'meta': {
            'linguistic': {
                'support': {
                    'noun': 'support',
                    'adjective': 'supported'
                }
            }
        },
        'expected': 'Let $f(x)$ be a real function where $x$ is a real variable, saying that $f(x)$ is supported for all $x$ from $a$ to $c$ where $a$ and $c$ are real constants, is equivalent of saying that $$f{\left (b \\right )} \\neq 0$$ is true for all $b$ such that $b$ is contained between $a$ and $c$ where $b$ is a real constant.'
    },
    {
        'test': {},
        'data': {
            'id': 'compact_support',
            'input': [
                {
                    'symbols': ['f'],
                    'type': 'real',
                    'kind': 'function',
                    'dependencies': ['x']
                }
            ],
            'equivalence': [
                {
                    'function': ['f'],
                    'is': ['compact_support'],
                    'of': {
                        'symbol': 'x',
                        'from': 'a',
                        'to': 'c'
                    }
                },
                {
                    'and': [
                        {
                            'function': ['f'],
                            'is': ['support'],
                            'of': {
                                'symbol': 'x',
                                'from': 'a',
                                'to': 'c'
                            }
                        },
                        {
                            'expression': {
                                'operator': 'eq',
                                'lhs': 'f(b)',
                                'rhs': '0'
                            },
                            'forall': ['b']
                        }
                    ]
                }
            ],
            'symbols': [
                {
                    'symbols': ['x'],
                    'type': 'real',
                    'kind': 'variable'
                },
                {
                    'symbols': ['a', 'b', 'c'],
                    'type': 'real',
                    'kind': 'constant',
                    'constraints': [
                        {
                            'symbol': 'b',
                            'type': 'outside',
                            'lb': 'a',
                            'ub': 'c'
                        }
                    ]
                }
            ]
        },
        'meta': {
            'linguistic': {
                'support': {
                    'noun': 'support',
                    'adjective': 'supported'
                },
                'compact_support': {
                    "noun": "compact support",
                    "adjective": "compactly supported"
                }
            }
        },
        'expected': 'Let $f(x)$ be a real function where $x$ is a real variable, saying that $f(x)$ is compactly supported for all $x$ from $a$ to $c$ where $a$ and $c$ are real constants, is equivalent of saying that $f(x)$ is supported for all $x$ from $a$ to $c$ and $$f{\left (b \\right )} = 0$$ is true for all $b$ where $b$ is a real constant such that $b$ is not contained between $a$ and $c$.'
    },
    {
        'test': {},
        'data': {
            'id': 'continuity_at_point',
            'input': [
                {
                    'symbols': ['f'],
                    'type': 'real',
                    'kind': 'function',
                    'dependencies': ['x']
                }
            ],
            'equivalence': [
                {
                    'function': ['f'],
                    'is': ['continuity'],
                    'of': {
                        'symbol': 'x',
                        'at': 'c'
                    }
                },
                {
                    'expression': {
                        'operator': 'eq',
                        'lhs': 'Limit(f(x), x, c)',
                        'rhs': 'f(c)'
                    }
                }
            ],
            'symbols': [
                {
                    'symbols': ['x'],
                    'type': 'real',
                    'kind': 'variable'
                },
                {
                    'symbols': ['c'],
                    'type': 'real',
                    'kind': 'constant'
                }
            ]
        },
        'meta': {
            'linguistic': {
                'continuity': {
                    'noun': 'continuity',
                    'adjective': 'continuous'
                }
            }
        },
        'expected': 'Let $f(x)$ be a real function where $x$ is a real variable, saying that $f(x)$ is continuous for all $x$ at $c$ where $c$ is a real constant, is equivalent of saying that $$\\lim_{x \\to c^+} f{\\left (x \\right )} = f{\\left (c \\right )}$$ is true.'
    },
    {
        'test': {},
        'data': {
            'id': 'continuity_over_interval',
            'input': [
                {
                    'symbols': ['f'],
                    'type': 'real',
                    'kind': 'function',
                    'dependencies': ['x']
                }
            ],
            'equivalence': [
                {
                    'function': ['f'],
                    'is': ['continuity'],
                    'of': {
                        'symbol': 'x',
                        'from': 'a',
                        'to': 'b'
                    }
                },
                {
                    'function': ['f'],
                    'is': ['continuity'],
                    'of': {
                        'symbol': 'x',
                        'at': 'a'
                    }
                }
            ],
            'symbols': [
                {
                    'symbols': ['x'],
                    'type': 'real',
                    'kind': 'variable'
                },
                {
                    'symbols': ['a', 'b', 'c'],
                    'type': 'real',
                    'kind': 'constant',
                    'constraints': [
                        {
                            'symbol': 'b',
                            'type': 'inside',
                            'lb': 'a',
                            'ub': 'c'
                        }
                    ]
                }
            ]
        },
        'meta': {
            'linguistic': {
                'continuity': {
                    'noun': 'continuity',
                    'adjective': 'continuous'
                }
            }
        },
        'expected': 'Let $f(x)$ be a real function where $x$ is a real variable, saying that $f(x)$ is continuous for all $x$ from $a$ to $c$ where $a$ and $c$ are real constants is equivalent of saying that $f(x)$ is continuous for all $x$ at $b$ where $b$ is a real constant contained between $a$ and $c$.
    },
    {
        'test': {},
        'data': {
            'id': 'nth_order_continuity',
            'parameters': ['n'],
            'input': [
                {
                    'symbols': ['f'],
                    'type': 'real',
                    'kind': 'function',
                    'dependencies': ['x']
                },
                {
                    'symbols': ['n', 'k'],
                    'type': 'integer',
                    'kind': 'constant',
                    'assumptions': ['positive'],
                    'constraints': [
                        {
                            'type': 'geq',
                            'lhs': 'n',
                            'rhs': 'k'
                        }
                    ]
                }
            ],
            'equivalence': [
                {
                    'and': [
                        {
                            'function': ['f'],
                            'is': ['continuity'],
                            'of': {
                                'symbol': 'x',
                                'from': 'a',
                                'to': 'b'
                            }
                        },
                        {
                            'function': ['derivative(f(x), x, k)'],
                            'is': ['continuity'],
                            'of': {
                                'symbol': 'x',
                                'from': 'a',
                                'to': 'b'
                            },
                            'forall': ['k']
                        }
                    ],
                },
                {
                    'function': ['f'],
                    'is': ['nth_order_continuity'],
                    'of': {
                        'symbol': 'x',
                        'from': 'a',
                        'to': 'b'
                    }
                }
            ],
            'symbols': [
                {
                    'symbols': ['x'],
                    'type': 'real',
                    'kind': 'variable'
                },
                {
                    'symbols': ['a', 'b'],
                    'type': 'real',
                    'kind': 'constant',
                    'constraints': [
                        {
                            'type': 'gt',
                            'lhs': 'b',
                            'rhs': 'a'
                        }
                    ]
                }
            ]
        },
        'meta': {
            'derivative(f(x), x, k)': '$\\frac{d^k}{dx^k}f(x)$',
            'linguistic': {
                'continuity': {
                    'noun': 'continuity',
                    'adjective': 'continuous'
                },
                'nth_order_continuity': {
                    'noun': '$n$\'th order continuity',
                    'adjective': '$n$\'th order continuous'
                }
            }
        },
        'expected': 'Let $f(x)$ be a real function where $x$ is a real constant and let $n$ and $k$ be positives integer constants such that $n$ is greater or equal than $k$ where $k$ is a real constant, saying that $f(x)$ is continuous for all $x$ from $a$ to $b$ where $a$ and $b$ are real constants such that $b$ is strictly greater than $a$ and $\\frac{d^k}{dx^k}f(x)$ is continuous for all $x$ from $a$ to $b$ and for all $k$ is equivalent of saying that $f(x)$ is $n$\'th order continuous for all $x$ from $a$ to $b$.'
    },
    {
        'test': {},
        'data': {
            'input': [
                {
                    'symbols': ['f'],
                    'type': 'real',
                    'kind': 'function',
                    'dependencies': ['x']
                }
            ],
            'equivalence': [
                {
                    'and': [
                        {
                            'function': ['f'],
                            'is': ['nth_order_continuity'],
                            'of': {
                                'symbol': 'x',
                                'from': 'a',
                                'to': 'b'
                            }
                        },
                        {
                            'symbol': 'n',
                            'is': ['infinity']
                        }
                    ]
                },
                {
                    'function': ['f'],
                    'is': ['infinite_order_continuity'],
                    'of': {
                        'symbol': 'x',
                        'from': 'a',
                        'to': 'b'
                    }
                }
            ],
            'symbols': [
                {
                    'symbols': ['x'],
                    'type': 'real',
                    'kind': 'variable'
                },
                {
                    'symbols': ['a', 'b'],
                    'type': 'real',
                    'kind': 'constant',
                    'constraints': [
                        {
                            'type': 'gt',
                            'lhs': 'b',
                            'rhs': 'a'
                        }
                    ]
                }
            ]
        },
        'meta': {
            'linguistic': {
                'nth_order_continuity': {
                    'noun': '$n$\'th order continuity',
                    'adjective': '$n$\'th order continuous'
                },
                'infinite_order_continuity': {
                    'noun': 'infinite order continuity',
                    'adjective': 'infinite order continuous'
                }
            }
        },
        'expected': 'Let $f(x)$ be a real function where $x$ is a real variable, saying that $f(x)$ is $n$\'th order continuous for all $x$ from $a$ to $b$ where $n$ is infinite and $a$ and $b$ are real constants such that $b$ is strictly greater than $a$ is equivalent of saying that $f(x)$ is infinite order continuous for all $x$ from $a$ to $b$.'
    },
    {
        'test': {},
        'data': {
            'input': [
                {
                    'symbols': ['f'],
                    'type': 'real',
                    'kind': 'function',
                    'dependencies': ['x']
                }
            ],
            'equivalence': [
                {
                    'function': ['f'],
                    'is': ['infinite_order_continuity'],
                    'of': {
                        'symbol': 'x',
                        'from': 'a',
                        'to': 'b'
                    }
                },
                {
                    'function': ['f'],
                    'is': ['smoothness'],
                    'of': {
                        'symbol': 'x',
                        'from': 'a',
                        'to': 'b'
                    }
                }
            ],
            'symbols': [
                {
                    'symbols': ['x'],
                    'type': 'real',
                    'kind': 'variable'
                },
                {
                    'symbols': ['a', 'b'],
                    'type': 'real',
                    'kind': 'constant',
                    'constraints': [
                        {
                            'type': 'gt',
                            'lhs': 'b',
                            'rhs': 'a'
                        }
                    ]
                }
            ]
        },
        'meta': {
            'linguistic': {
                'smoothness': {
                    'noun': 'smoothness',
                    'adjective': 'smooth'
                },
                'infinite_order_continuity': {
                    'noun': 'infinite order continuity',
                    'adjective': 'infinite order continuous'
                }
            }
        },
        'expected': 'Let $f(x)$ be a real function where $x$ is a real variable, saying that $f(x)$ is infinite order continuous for all $x$ from $a$ to $b$ where $a$ and $b$ are constants such that $b$ is strictly greater than $a$ is equivalent of saying that $f(x)$ is smooth for all $x$ from $a$ to $b$.'
    },
    {
        'test': {},
        'data': {
            'input': [
                {
                    'symbols': ['f', 'h'],
                    'type': 'real',
                    'kind': 'function',
                    'dependencies': ['x']
                }
            ],
            'if': {
                'and': [
                    {
                        'function': ['f'],
                        'is': ['continuity'],
                        'of': {
                            'symbol': 'x',
                            'from': 'a',
                            'to': 'b'
                        }
                    },
                    {
                        'function': ['h'],
                        'is': ['compact_support'],
                        'of': {
                            'symbol': 'x',
                            'from': 'a',
                            'to': 'b'
                        }
                    },
                    {
                        'expression': {
                            'operator': 'eq',
                            'lhs': 'Integral(f(t)*h(t), (x, a, b))',
                            'rhs': '0'
                        }
                    }
                ]
            },
            'then': {
                'expression': {
                    'operator': 'eq',
                    'lhs': 'f(t)',
                    'rhs': '0'
                }
            },
            'symbols': [
                {
                    'symbols': ['x', 't'],
                    'type': 'real',
                    'kind': 'variable'
                },
                {
                    'symbols': ['a', 'b'],
                    'type': 'real',
                    'kind': 'constant',
                    'constraints': [
                        {
                            'type': 'gt',
                            'lhs': 'b',
                            'rhs': 'a'
                        }
                    ]
                }
            ]
        },
        'meta': {
            'linguistic': {
                'compact_support': {
                    'noun': 'compact support',
                    'adjective': 'compactly supported'
                },
                'continuity': {
                    'noun': 'continuity',
                    'adjective': 'continuous'
                }
            }
        },
        'expected': 'Let $f(x)$ and $h(x)$ be real functions where $x$ is a real variable such that if $f(x)$ is continuous for all $x$ from $a$ to $b$ where $a$ and $b$ are constants such that $b$ is strictly greater than $a$, $h(x)$ is compactly supported for all $x$ from $a$ to $b$ and $$\\int_{a}^{b} f{\\left (t \\right )} h{\\left (t \\right )}\, dx = 0$$ is true then $$f{\left (t \\right )} = 0$$ is true.'
    }
]

@parametrized(*tests)
class IntegrationTest(TestCase) :
    def testIntegration(self) :
        if skipTest(self.test) : return skip('test disabled')
        output = surfaceRealize(self.data, self.meta)
        assertEqual(self, output, self.expected)
    def setParameters(self, test, data, meta, expected):
        self.test = test
        self.data = data
        self.meta = meta
        self.expected = expected
