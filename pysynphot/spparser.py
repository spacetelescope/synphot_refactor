# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
This file implements the pysynphot language parser.

The language definition is in the docstring of class BaseParser,
function p_top.  The parser code in spark.py builds its internal
tables by reading the docstring, so you can't put anything else
(like documentation) there.
::

  l = scan('text') returns a list of tokens

  t = parse(l) converts the list of tokens into an Abstract Syntax Tree

  r = interpret(t) converts that abstract syntax tree into a (tree
    of?) pysynphot object, based on the conversion rules in class Interpreter

In class Interpreter, the docstring of every function named with p\_
is part of the instructions to the parser.

"""

from __future__ import division, print_function

from . import spark
from . import spectrum
from . import reddening
from . import locations
from . import catalog
from . import obsbandpass
from . import pysynexcept

syfunctions = [
    'spec',
    'unit',
    'box',
    'bb',
    'pl',
    'em',
    'icat',
    'rn',
    'z',
    'ebmvx',
    'band'
]

synforms = [
    'fnu',
    'flam',
    'photnu',
    'photlam',
    'counts',
    'abmag',
    'stmag',
    'obmag',
    'vegamag',
    'jy',
    'mjy'
]

syredlaws = [
    'gal1',
    'gal2',
    'gal3',
    'smc',
    'lmc',
    'xgal'
]


class Token:
    def __init__(self, type=None, attr=None):
        self.type = type
        self.attr = attr

    def __cmp__(self, o):
        return cmp(self.type, o)

    def __repr__(self):
        if self.attr is not None:
            return str(self.attr)
        else:
            return self.type


class AST:
    def __init__(self, type):
        self.type = type
        self._kids = []

    def __getitem__(self, i):
        return self._kids[i]

    def __len__(self):
        return len(self._kids)

    def __setslice__(self, low, high, seq):
        self._kids[low:high] = seq

    def __cmp__(self, o):
        return cmp(self.type, o)


class BaseScanner(spark.GenericScanner):
    def __init__(self):
        spark.GenericScanner.__init__(self)

    def tokenize(self, input):
        self.rv = []
        spark.GenericScanner.tokenize(self, input)
        return self.rv

    def t_whitespace(self, s):
        r' \s+ '

    def t_op(self, s):
        r' \+ | \* | - '
        self.rv.append(Token(type=s))

    def t_lparens(self, s):
        r' \( '
        self.rv.append(Token(type='LPAREN'))

    def t_rparens(self, s):
        r' \) '
        self.rv.append(Token(type='RPAREN'))

    def t_comma(self, s):
        r' , '
        self.rv.append(Token(type=s))

    def t_integer(self, s):
        r' \d+ '
        self.rv.append(Token(type='INTEGER', attr=s))

    def t_identifier(self, s):
        r' [$a-z_A-Z/\//][\w/\.\$:#]*'
        self.rv.append(Token(type='IDENTIFIER', attr=s))

    def t_filelist(self, s):
        r' @\w+'
        self.rv.append(Token(type='FILELIST', attr=s[1:]))


class Scanner(BaseScanner):
    def __init__(self):
        BaseScanner.__init__(self)

    def t_float(self, s):
        r' ((\d*\.\d+)|(\d+\.d*)|(\d+)) ([eE][-+]?\d+)?'
        self.rv.append(Token(type='FLOAT', attr=s))

    def t_divop(self, s):
        r' \s/\s '
        self.rv.append(Token(type='/'))


class BaseParser(spark.GenericASTBuilder):
    def __init__(self, ASTclass, start='top'):
        spark.GenericASTBuilder.__init__(self, ASTclass, start)

    def p_top(self, args):
        """
            top ::= expr
            top ::= FILELIST
            expr ::= expr + term
            expr ::= expr - term
            expr ::= term
            term ::= term * factor
            term ::= term / factor
            value ::= LPAREN expr RPAREN
            term ::= factor
            factor ::= unaryop value
            factor ::= value
            unaryop ::= +
            unaryop ::= -
            value ::= INTEGER
            value ::= FLOAT
            value ::= IDENTIFIER
            value ::= function_call
            function_call ::= IDENTIFIER LPAREN arglist RPAREN
            arglist ::= arglist , expr
            arglist ::= expr
        """

    def terminal(self, token):
        rv = AST(token.type)
        rv.attr = token.attr
        return rv

    def nonterminal(self, type, args):
        if len(args) == 1:
            return args[0]
        return spark.GenericASTBuilder.nonterminal(self, type, args)


class Interpreter(spark.GenericASTMatcher):
    def __init__(self, ast):
        spark.GenericASTMatcher.__init__(self, 'V', ast)

    def error(self, token):
        raise ValueError("problems in interpreting AST")

    def p_int(self, tree):
        """
        V ::= INTEGER

        """
        tree.value = int(tree.attr)
        tree.svalue = tree.attr

    def p_float(self, tree):
        """
        V ::= FLOAT

        """
        tree.value = float(tree.attr)
        tree.svalue = tree.attr

    def p_identifier(self, tree):
        """
        V ::= IDENTIFIER

        """
        tree.value = tree.attr
        tree.svalue = tree.attr

    def p_factor_unary_plus(self, tree):
        """
        V ::= factor ( + V )

        """
        tree.value = convertstr(tree[1].value)

    def p_factor_unary_minus(self, tree):
        """
        V ::= factor ( - V )

        """
        tree.value = - convertstr(tree[1].value)

    def p_expr_plus(self, tree):
        """
        V ::= expr ( V + V )

        """
        tree.value = convertstr(tree[0].value) + convertstr(tree[2].value)

    def p_expr_minus(self, tree):
        """
        V ::= expr ( V - V )

        """
        tree.value = convertstr(tree[0].value) - convertstr(tree[2].value)

    def p_term_mult(self, tree):
        """
        V ::= term ( V * V )

        """
        tree.value = convertstr(tree[0].value) * convertstr(tree[2].value)

    def p_term_div(self, tree):
        """
        V ::= term ( V / V )

        """
        tree.value = convertstr(tree[0].value) / tree[2].value

    def p_value_paren(self, tree):
        """
        V ::= value ( LPAREN V RPAREN )

        """
        tree.value = convertstr(tree[1].value)
        tree.svalue = "(%s)" % str(tree[1].value)

    def p_arglist(self, tree):
        """
        V ::= arglist ( V , V )

        """
        if isinstance(tree[0].value, list):
            tree.value = tree[0].value + [tree[2].value]
        else:
            tree.value = [tree[0].value, tree[2].value]
        try:
            tree.svalue = "%s,%s" % (tree[0].svalue, tree[2].svalue)
        except AttributeError:
            pass  # We only care about this for relatively simple constructs.

    def p_functioncall(self, tree):
        # Where all the real interpreter action is
        # Note that things that should only be done at the top level
        # are performed in the interpret function defined below.
        """
        V ::= function_call ( V LPAREN V RPAREN )

        """
        if type(tree[2].value)!=type([]):
            args = [tree[2].value]
        else:
            args = tree[2].value
        fname = tree[0].value
        if fname not in syfunctions:
            print("Error: unknown function:", fname)
            self.error(fname)
        else:
            if fname == 'unit':
                # constant spectrum
                tree.value = spectrum.FlatSpectrum(args[0], fluxunits=args[1])
            elif fname == 'bb':
                # black body
                tree.value = spectrum.BlackBody(args[0])
            elif fname == 'pl':
                # power law
                if args[2] not in synforms:
                    print("Error: unrecognized units:", args[2])
                # code to create powerlaw spectrum object
                tree.value = spectrum.Powerlaw(args[0], args[1],
                                               fluxunits=args[2]
                )
            elif fname == 'box':
                # box throughput
                tree.value = spectrum.Box(args[0], args[1])
            elif fname == 'spec':
                # spectrum from reference file (for now....)
                name = args[0]
                tree.value = spectrum.TabularSourceSpectrum(
                    _handleIRAFName(name)
                )
            elif fname == 'band':
                # passband
                args = tree[2].svalue
                tree.value = obsbandpass.ObsBandpass(args)
            elif fname == 'em':
                # emission line
                tree.value = spectrum.GaussianSource(args[2], args[0],
                                                     args[1], fluxunits=args[3])
            elif fname == 'icat':
                # catalog interpolation
                tree.value = catalog.Icat(*args)
            elif fname == 'rn':
                # renormalize
                sp = args[0]
                if not isinstance(sp,spectrum.SourceSpectrum):
                    name = _handleIRAFName(args[0])
                    sp = spectrum.TabularSourceSpectrum(name)

                # Always force the renormalization to occur: prevent exceptions
                # in case of partial overlap. Less robust but duplicates
                # synphot. Force the renormalization in the case of partial
                # overlap (pysynexcept.OverlapError), but raise an exception if
                # the spectrum and bandpass are entirely disjoint
                # (pysynexcept.DisjoinError)
                try:
                    tree.value = sp.renorm(args[2], args[3], args[1])
                except pysynexcept.DisjoinError:
                    raise
                except pysynexcept.OverlapError:
                    tree.value = sp.renorm(args[2], args[3],
                                           args[1], force=True)
                    tree.value.warnings['force_renorm'] = \
                        'Warning: Renormalization of the spectrum, ' \
                        'to the specified value, in the specified units, ' \
                        'exceeds the limit of the specified passband.'

            elif fname == 'z':
                # redshift
                if args[0] != 'null':  # the ETC generates junk sometimes....
                    try:
                        tree.value = args[0].redshift(args[1])
                    except AttributeError:
                        try:
                            sp = spectrum.TabularSourceSpectrum(
                                _handleIRAFName(args[0])
                            )
                            tree.value = sp.redshift(args[1])
                        except AttributeError:
                            tree.value = spectrum.FlatSpectrum(1.0)
                else:
                    tree.value = spectrum.FlatSpectrum(1.0)
            elif fname == 'ebmvx':
                # extinction
                tree.value = reddening.Extinction(args[0], args[1])

            else:
                tree.value = "would call %s with the following args: %s" % \
                             (fname, repr(args))


# stuff not yet handled, namely, Filelist, should be handled in interp function
zzz = """ top ::= FILELIST """


def convertstr(value):
    # Any string appearing in numeric expressions must be
    # assumed to be a filename that should be read in as a table
    # This is a utility function used by the interpreter to do the
    # conversion from string to spectrum object
    if isinstance(value, str):
        return _handleThroughputFiles(_handleIRAFName(value))
    else:
        return value


def scan(input):
    scanner = Scanner()
    input = input.replace('%2b', '+')
    return scanner.tokenize(input)


def parse(tokens):
    parser = BaseParser(AST)
    return parser.parse(tokens)


def interpret(ast):
    interpreter = Interpreter(ast)
    interpreter.match()
    value = ast.value
    return convertstr(value)


def ptokens(tlist):
    for token in tlist:
        print(token.type, token.attr)


def _handleIRAFName(name):
    """
    Calls locations.irafconvert() to translate shell or iraf variables

    """

    return locations.irafconvert(name)


def _handleThroughputFiles(name):
    #Most files will be spectrum files, but some will be throughput files.
    try:
        return spectrum.TabularSourceSpectrum(_handleIRAFName(name))
    except NameError:
        return spectrum.TabularSourceSpectrum(_handleIRAFName(name))


#Convenience function
def parse_spec(syncommand):
    """
    Parse the synphot-classic command and return the resulting spectrum

    """
    sp = interpret(parse(scan(syncommand)))
    return sp
