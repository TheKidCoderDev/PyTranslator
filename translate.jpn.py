!/usr/ビン/env python3

インポート sys
インポート re

グローバル characters, translations

translations=[
    [
      "False",
      "class",
      "finally",
      "is",
      "return",
      "None",
      "continue",
      "for",
      "lambda",
      "try",
      "True",
      "def",
      "from",
      "nonlocal",
      "while",
      "and",
      "del",
      "global",
      "not",
      "with",
      "as",
      "elif",
      "or",
      "yield",
      "assert",
      "else",
      "import",
      "pass",
      "break",
      "except",
      "if",
      "raise",
      "await",
      "async",
      "in",
      "abs",
      "delattr",
      "hash",
      "memoryview",
      "set",
      "all",
      "dict",
      "help",
      "min",
      "setattr",
      "any",
      "dir",
      "hex",
      "next",
      "slice",
      "ascii",
      "divmod",
      "id",
      "object",
      "sorted",
      "bin",
      "enumerate",
      "input",
      "oct",
      "staticmethod",
      "bool",
      "eval",
      "int",
      "open",
      "str",
      "breakpoint",
      "exec",
      "isinstance",
      "ord",
      "sum",
      "bytearray",
      "filter",
      "issubclass",
      "pow",
      "super",
      "bytes",
      "float",
      "iter",
      "print",
      "tuple",
      "callable",
      "format",
      "len",
      "property",
      "type",
      "chr",
      "frozenset",
      "list",
      "range",
      "vars",
      "classmethod",
      "getattr",
      "locals",
      "repr",
      "zip",
      "compile",
      "globals"
      "map",
      "reversed",
      "__インポート__",
      "complex",
      "hasattr"
      "max",
      "round"
    ],
    [
        "偽",
        "クラス",
        "最後に",
        "です",
        "戻る",
        "無し",
        "持続する",
        "にとって",
        "ラムダ",
        "やってみる",
        "本当の",
        "定義する",
        "から",
        "非局所的",
        "しながら",
        "そして",
        "削除する",
        "グローバル",
        "ではない",
        "と",
        "として",
        "そうでなければ",
        "または",
        "産出",
        "アサート",
        "それ以外の",
        "インポート",
        "パス",
        "ブレーク",
        "を除く",
        "もし",
        "上げる",
        "待つ",
        "非同期",
        "に",
        "絶対の",
        "デラッタ",
        "ハッシュ",
        "記憶_見る",
        "セット",
        "すべて",
        "口述",
        "助けて",
        "最小",
        "セット_属性",
        "どれか",
        "方向",
        "ヘックス",
        "次",
        "スライス",
        "アスキー",
        "分ける_変形",
        "識別する",
        "物",
        "ソート済み",
        "ビン",
        "列挙する",
        "入力",
        "十",
        "静的_方法",
        "ブール値",
        "評価する",
        "整数",
        "開いた",
        "ひも",
        "ブレークポイント",
        "執行部",
        "です_実例",
        "序",
        "和",
        "バイト配列",
        "フィルタ",
        "サブクラスです",
        "捕虜",
        "スーパー",
        "バイト",
        "浮く",
        "それより",
        "印刷する",
        "タプル",
        "呼び出し可能",
        "フォーマット",
        "レン",
        "財産",
        "タイプ",
        "チャー",
        "冷凍セット",
        "リスト",
        "範囲",
        "変数",
        "クラス方法",
        "ゲッタ",
        "地元の人",
        "報いる",
        "ジップ",
        "コンパイル",
        "_グローバル",
        "地図",
        "逆転",
        "__インポート__",
        "複雑な",
        "持っている_属性",
        "最大",
        "円形"
    ],
    [
      'faux',
      'classe',
      'finalement',
      'est',
      'retourn',
      'rien',
      'continue',
      'pour',
      'lambda',
      'essaye',
      'vraie',
      'definir',
      'de',
      'pas_local',
      'pendant',
      'et',
      'effacer',
      'globale',
      'pas',
      'avec',
      'aussi',
      'autre_si',
      'ou',
      'faire_attention',
      'affirmer',
      'autre',
      'viens_de',
      'passe',
      'pause',
      'autrement',
      'si',
      'elever',
      'attendre',
      'asynchrone',
      'dans',
      'absolu',
      'effacer_attribut',
      'hash',
      'memoire_vue',
      'mis',
      'tous',
      'dictionaire',
      'aide',
      'minimum',
      'mis_attibut',
      'tout',
      'directoire',
      'hex',
      'suivant',
      'morceaux',
      'ascii',
      'divise_modification',
      'identification',
      'objet',
      'tries',
      'binaire',
      'compter',
      'input',
      'huit',
      'static_methode ',
      'booleen',
      'evalue',
      'entier',
      'ouvert',
      'chaine',
      'point_darret',
      'faire',
      'est_instance',
      'ordre',
      'total',
      'octet_tableau',
      'filtre',
      'est_duexiemeclasse',
      'exposant',
      'superbe',
      'bytes',
      'float',
      'repeter',
      'impression',
      'tuple',
      'appelable',
      'format',
      'grandeur',
      'propriete',
      'type',
      'charactere',
      'glacer_',
      'liste',
      'intervalle',
      'variables',
      'classe_methode',
      'recevoire_attribut',
      'locales',
      'represent',
      'zip',
      'compiler',
      'globales',
      'carte',
      'renversé',
      '__importation__',
      'complexe',
      'a_attribut',
      'maximum',
      'rond'
    ]
]

possibleQuotes=['"', "'", '"""', "'''"]

定義する split(word):
    i = [char にとって char に word]
    r = ''
    x=[]
    にとって e に i:
        もし e ではない に possibleQuotes または e に possibleQuotes そして i[i.index(e)-1] == '\\' そして i[i.index(e)-2] != '\\':
            r+=e
        それ以外の:
            x.append(r)
            x.append(e)
            r=''
    x.append(r)
    戻る x


characters = [
    "!",
    "$",
    "%",
    "&",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
    "\n",
    "\t",
    "   ",
    " "
]

"""
filename = sys.argv[1]

もし filename.endswith(".jp.py"):
    jp=本当の
それ以外の:
    jp=偽
"""

グローバル data
data=3

re

定義する run(filename, startlang='0', endlang='2'):
    グローバル data
    と 開いた(filename) として a:
        グローバル data
        data=a.read()

    data+="\n"+data
    strStatus={
        "mla": 偽,
        "a": 偽,
        "mlq": 偽,
        "q": 偽,
    }

    strChar=無し

    もし startlang == endlang:
        印刷する("Please select different languages")
    それ以外の:
        にとって i に translations[startlang]:
            にとって l に characters:
                にとって r に characters:
                    もし ではない strStatus["mla"] または strStatus["mlq"] または strStatus["a"] または strStatus["q"]:
                        もし "'''" に i:
                            strStatus["mla"] = ではない strStatus["mla"]
                        そうでなければ '"""' に i:
                            strStatus["mlq"] = ではない strStatus["mlq"]
                        そうでなければ '"' に i:
                            strStatus["q"]= ではない strStatus["q"]
                        そうでなければ "'" に i:
                            strStatus["a"]= ではない strStatus["a"]
                        それ以外の:
                            data = data.replace(l+i+r, l+translations[endlang][translations[startlang].index(i)]+r)

# /("(?:[^"\\]+|\\.)*")|('(?:[^'\\]+|\\.)*')|(#.*)/g (RegEx にとって strings そして comments)


    filename = filename.split('.')[0]
    numtocode={
        0: "eng",
        1: "jpn",
        2: "fr"
    }
    filename+="."+numtocode[endlang]+".py"
    data=data[1:]

    と 開いた(filename,"w+") として f:
        f.write(data)

    印刷する("Translated to file {}".フォーマット(filename))

#!/usr/ビン/env python3

インポート sys
インポート re

グローバル characters, translations

translations=[
    [
      "False",
      "class",
      "finally",
      "is",
      "return",
      "None",
      "continue",
      "for",
      "lambda",
      "try",
      "True",
      "def",
      "from",
      "nonlocal",
      "while",
      "and",
      "del",
      "global",
      "not",
      "with",
      "as",
      "elif",
      "or",
      "yield",
      "assert",
      "else",
      "import",
      "pass",
      "break",
      "except",
      "if",
      "raise",
      "await",
      "async",
      "in",
      "abs",
      "delattr",
      "hash",
      "memoryview",
      "set",
      "all",
      "dict",
      "help",
      "min",
      "setattr",
      "any",
      "dir",
      "hex",
      "next",
      "slice",
      "ascii",
      "divmod",
      "id",
      "object",
      "sorted",
      "bin",
      "enumerate",
      "input",
      "oct",
      "staticmethod",
      "bool",
      "eval",
      "int",
      "open",
      "str",
      "breakpoint",
      "exec",
      "isinstance",
      "ord",
      "sum",
      "bytearray",
      "filter",
      "issubclass",
      "pow",
      "super",
      "bytes",
      "float",
      "iter",
      "print",
      "tuple",
      "callable",
      "format",
      "len",
      "property",
      "type",
      "chr",
      "frozenset",
      "list",
      "range",
      "vars",
      "classmethod",
      "getattr",
      "locals",
      "repr",
      "zip",
      "compile",
      "globals"
      "map",
      "reversed",
      "__インポート__",
      "complex",
      "hasattr"
      "max",
      "round"
    ],
    [
        "偽",
        "クラス",
        "最後に",
        "です",
        "戻る",
        "無し",
        "持続する",
        "にとって",
        "ラムダ",
        "やってみる",
        "本当の",
        "定義する",
        "から",
        "非局所的",
        "しながら",
        "そして",
        "削除する",
        "グローバル",
        "ではない",
        "と",
        "として",
        "そうでなければ",
        "または",
        "産出",
        "アサート",
        "それ以外の",
        "インポート",
        "パス",
        "ブレーク",
        "を除く",
        "もし",
        "上げる",
        "待つ",
        "非同期",
        "に",
        "絶対の",
        "デラッタ",
        "ハッシュ",
        "記憶_見る",
        "セット",
        "すべて",
        "口述",
        "助けて",
        "最小",
        "セット_属性",
        "どれか",
        "方向",
        "ヘックス",
        "次",
        "スライス",
        "アスキー",
        "分ける_変形",
        "識別する",
        "物",
        "ソート済み",
        "ビン",
        "列挙する",
        "入力",
        "十",
        "静的_方法",
        "ブール値",
        "評価する",
        "整数",
        "開いた",
        "ひも",
        "ブレークポイント",
        "執行部",
        "です_実例",
        "序",
        "和",
        "バイト配列",
        "フィルタ",
        "サブクラスです",
        "捕虜",
        "スーパー",
        "バイト",
        "浮く",
        "それより",
        "印刷する",
        "タプル",
        "呼び出し可能",
        "フォーマット",
        "レン",
        "財産",
        "タイプ",
        "チャー",
        "冷凍セット",
        "リスト",
        "範囲",
        "変数",
        "クラス方法",
        "ゲッタ",
        "地元の人",
        "報いる",
        "ジップ",
        "コンパイル",
        "_グローバル",
        "地図",
        "逆転",
        "__インポート__",
        "複雑な",
        "持っている_属性",
        "最大",
        "円形"
    ],
    [
      'faux',
      'classe',
      'finalement',
      'est',
      'retourn',
      'rien',
      'continue',
      'pour',
      'lambda',
      'essaye',
      'vraie',
      'definir',
      'de',
      'pas_local',
      'pendant',
      'et',
      'effacer',
      'globale',
      'pas',
      'avec',
      'aussi',
      'autre_si',
      'ou',
      'faire_attention',
      'affirmer',
      'autre',
      'viens_de',
      'passe',
      'pause',
      'autrement',
      'si',
      'elever',
      'attendre',
      'asynchrone',
      'dans',
      'absolu',
      'effacer_attribut',
      'hash',
      'memoire_vue',
      'mis',
      'tous',
      'dictionaire',
      'aide',
      'minimum',
      'mis_attibut',
      'tout',
      'directoire',
      'hex',
      'suivant',
      'morceaux',
      'ascii',
      'divise_modification',
      'identification',
      'objet',
      'tries',
      'binaire',
      'compter',
      'input',
      'huit',
      'static_methode ',
      'booleen',
      'evalue',
      'entier',
      'ouvert',
      'chaine',
      'point_darret',
      'faire',
      'est_instance',
      'ordre',
      'total',
      'octet_tableau',
      'filtre',
      'est_duexiemeclasse',
      'exposant',
      'superbe',
      'bytes',
      'float',
      'repeter',
      'impression',
      'tuple',
      'appelable',
      'format',
      'grandeur',
      'propriete',
      'type',
      'charactere',
      'glacer_',
      'liste',
      'intervalle',
      'variables',
      'classe_methode',
      'recevoire_attribut',
      'locales',
      'represent',
      'zip',
      'compiler',
      'globales',
      'carte',
      'renversé',
      '__importation__',
      'complexe',
      'a_attribut',
      'maximum',
      'rond'
    ]
]

possibleQuotes=['"', "'", '"""', "'''"]

定義する split(word):
    i = [char にとって char に word]
    r = ''
    x=[]
    にとって e に i:
        もし e ではない に possibleQuotes または e に possibleQuotes そして i[i.index(e)-1] == '\\' そして i[i.index(e)-2] != '\\':
            r+=e
        それ以外の:
            x.append(r)
            x.append(e)
            r=''
    x.append(r)
    戻る x


characters = [
    "!",
    "$",
    "%",
    "&",
    "(",
    ")",
    "*",
    "+",
    ",",
    "-",
    ".",
    "/",
    ":",
    ";",
    "<",
    "=",
    ">",
    "?",
    "@",
    "[",
    "\\",
    "]",
    "^",
    "_",
    "`",
    "{",
    "|",
    "}",
    "~",
    "\n",
    "\t",
    "   ",
    " "
]

"""
filename = sys.argv[1]

もし filename.endswith(".jp.py"):
    jp=本当の
それ以外の:
    jp=偽
"""

グローバル data
data=3

re

定義する run(filename, startlang='0', endlang='2'):
    グローバル data
    と 開いた(filename) として a:
        グローバル data
        data=a.read()

    data+="\n"+data
    strStatus={
        "mla": 偽,
        "a": 偽,
        "mlq": 偽,
        "q": 偽,
    }

    strChar=無し

    もし startlang == endlang:
        印刷する("Please select different languages")
    それ以外の:
        にとって i に translations[startlang]:
            にとって l に characters:
                にとって r に characters:
                    もし ではない strStatus["mla"] または strStatus["mlq"] または strStatus["a"] または strStatus["q"]:
                        もし "'''" に i:
                            strStatus["mla"] = ではない strStatus["mla"]
                        そうでなければ '"""' に i:
                            strStatus["mlq"] = ではない strStatus["mlq"]
                        そうでなければ '"' に i:
                            strStatus["q"]= ではない strStatus["q"]
                        そうでなければ "'" に i:
                            strStatus["a"]= ではない strStatus["a"]
                        それ以外の:
                            data = data.replace(l+i+r, l+translations[endlang][translations[startlang].index(i)]+r)

# /("(?:[^"\\]+|\\.)*")|('(?:[^'\\]+|\\.)*')|(#.*)/g (RegEx にとって strings そして comments)


    filename = filename.split('.')[0]
    numtocode={
        0: "eng",
        1: "jpn",
        2: "fr"
    }
    filename+="."+numtocode[endlang]+".py"
    data=data[1:]

    と 開いた(filename,"w+") として f:
        f.write(data)

    印刷する("Translated to file {}".フォーマット(filename))
