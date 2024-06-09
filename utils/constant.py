from utils.rules import KeyWord

KEYWORD = KeyWord()
ERROR_TOKEN = -100

GRAMMAR = {
    "program": [
        [
            "declaration_list"
        ]
    ],
    "declaration_list": [
        [
            "declaration",
            "declaration_list#"
        ]
    ],
    "declaration_list#": [
        [
            "declaration",
            "declaration_list#"
        ],
        [
            "empty"
        ]
    ],
    "declaration": [
        [
            "var_declaration"
        ],
        [
            "fun_declaration"
        ]
    ],
    "var_declaration": [
        [
            "type_specifier",
            "ID",
            "var_declaration#"
        ]
    ],
    "var_declaration#": [
        [
            "[",
            "NUM",
            "]",
            ";"
        ],
        [
            ";"
        ]
    ],
    "type_specifier": [
        [
            "int"
        ],
        [
            "void"
        ]
    ],
    "fun_declaration": [
        [
            "type_specifier",
            "ID",
            "(",
            "params",
            ")",
            "compound_stmt"
        ]
    ],
    "params": [
        [
            "param_list"
        ],
        [
            "void"
        ]
    ],
    "param_list": [
        [
            "param",
            "param_list#"
        ]
    ],
    "param_list#": [
        [
            ",",
            "param",
            "param_list#"
        ],
        [
            "empty"
        ]
    ],
    "param": [
        [
            "type_specifier",
            "ID",
            "param#"
        ]
    ],
    "param#": [
        [
            "[",
            "]"
        ],
        [
            "empty"
        ]
    ],
    "compound_stmt": [
        [
            "{",
            "local_declarations",
            "statement_list",
            "}"
        ]
    ],
    "local_declarations": [
        [
            "local_declarations#"
        ]
    ],
    "local_declarations#": [
        [
            "var_declaration",
            "local_declarations#"
        ],
        [
            "empty"
        ]
    ],
    "statement_list": [
        [
            "statement_list#"
        ]
    ],
    "statement_list#": [
        [
            "statement",
            "statement_list#"
        ],
        [
            "empty"
        ]
    ],
    "statement": [
        [
            "expression_stmt"
        ],
        [
            "compound_stmt"
        ],
        [
            "selection_stmt"
        ],
        [
            "iteration_stmt"
        ],
        [
            "return_stmt"
        ]
    ],
    "expression_stmt": [
        [
            "expression",
            ";"
        ],
        [
            ";"
        ]
    ],
    "selection_stmt": [
        [
            "if",
            "(",
            "expression",
            ")",
            "statement",
            "selection_stmt#"
        ]
    ],
    "selection_stmt#": [
        [
            "else",
            "statement"
        ],
        [
            "empty"
        ]
    ],
    "iteration_stmt": [
        [
            "while",
            "(",
            "expression",
            ")",
            "statement"
        ]
    ],
    "return_stmt": [
        [
            "return",
            "return_stmt#"
        ]
    ],
    "return_stmt#": [
        [
            "expression",
            ";"
        ],
        [
            ";"
        ],
    ],
    "expression": [
        [
            "ID",
            "expression#"
        ]
    ],
    "expression#": [
        [
            "=",
            "expression"
        ],
        [
            "term#",
            "additive_expression#",
            "simple_expression"
        ],
        [
            "call",
            "term#",
            "additive_expression#",
            "simple_expression"
        ]
    ],
    "simple_expression": [
        [
            "additive_expression",
            "simple_expression#"
        ]
    ],
    "simple_expression#": [
        [
            "relop",
            "additive_expression"
        ],
        [
            "empty"
        ]
    ],
    "relop": [
        [
            "<="
        ],
        [
            "<"
        ],
        [
            ">"
        ],
        [
            ">="
        ],
        [
            "=="
        ],
        [
            "!="
        ]
    ],
    "additive_expression": [
        [
            "term",
            "additive_expression#"
        ]
    ],
    "additive_expression#": [
        [
            "addop",
            "term",
            "additive_expression#"
        ],
        [
            "empty"
        ]
    ],
    "addop": [
        [
            "+"
        ],
        [
            "-"
        ]
    ],
    "term": [
        [
            "factor",
            "term#"
        ]
    ],
    "term#": [
        [
            "mulop",
            "factor",
            "term#"
        ],
        [
            "empty"
        ]
    ],
    "mulop": [
        [
            "*"
        ],
        [
            "/"
        ]
    ],
    "factor": [
        [
            "(",
            "expression",
            ")"
        ],
        [
            "ID",
            "call"
        ],
        [
            "NUM"
        ]
    ],
    "call": [
        [
            "(",
            "args",
            ")"
        ],
        [
            "empty"
        ]
    ],
    "args": [
        [
            "arg_list"
        ],
        [
            "empty"
        ]
    ],
    "arg_list": [
        [
            "expression",
            "arg_list#"
        ]
    ],
    "arg_list#": [
        [
            ",",
            "expression",
            "arg_list#"
        ],
        [
            "empty"
        ]
    ]
}