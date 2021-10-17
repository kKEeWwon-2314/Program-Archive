#!/usr/bin/env python3
"""
    Summary
This program is a python3 syntax analyzer for Karel programs that checks for
the presence of certain Karel-specific elements and limits the usage of
python language constructs to those specified in the Karel instruction set,
outputting any errors or warnings it finds.

Note that some errors that are found may have a cascading effect,
causing many other errors to be detected in the rest of the file.


    Usage
Running this program with the path to any readable file as an argument
will begin analysis of that file, outputting errors.

Passing a directory name instead of a file name will make the program
search the directory and analyze all .py python files in it.

Multiple arguments will apply the above to each argument.

When the program is run with no arguments, it will search the directory
that the program was called from for .py files to analyze, which is
equivalent to passing '.' as a directory path.

The analysis functions are also available as an import, using
karelanalyzer.analyze(filename) for file analysis, and
karelanalyzer.analyzedir(path) for directory searching.


    Details
This analyzer strictly enforces a number of things, including:

- 'from karel import *' must be called before begin_karel_program.
    Note that 'import karel' will not be recognized by the program.

- begin_karel_program must be called once before any statements,
    other than instruction definitions.

- end_karel_program must be called once at base depth.
    That is, it must not be indented. See warnings below for details.

- Besides the above exceptions, all lines must begin with one of:
    - def, while, for, if, else
    - # or a multiline comment
    - one of the defined functions listed in the analyze function
    - or a user defined instruction.
    All other statements are marked as an error, regardless
    of if they are correct python or not.

- Proper syntax for these statements.
    Note that the Karel syntax for these differ from the actual
    python syntax requirements. The program takes advantage of
    the limited instruction set to simplify syntax checks.

- 'def' instruction definitions must be after the karel import
    and before the begin_karel_program call.

- The conditional statements for while and if must be
    one of the listed conditional functions below, or it will
    be marked as an error, 'True' and 'False' included.

- Similarly, 'while' and 'if' statements are limited to exactly one
    argument, meaning that 'and' and 'or' are marked as errors.
    'not' is an exception, and can be used.

It also provides warnings when:
- Lines are indented using tabs.
- Lines are unnecessarily indented.
- Unindented lines do not match any outer indentation levels.
- Statements are made after 'end_karel_program' is called.
- There is an unterminated multiline comment by the end of the file.
- 'from karel import *' is called more than once.
- Instruction definitions are nested.
- 'end_karel_program' is nested.
    This particular behavior may or may not be an error depending
    on the specifications, so it is listed as a warning in this case.


Created by Adrian Chen, 2018/09
Integration into the base karel distribution by Sonny Chan, 2020/03
"""

# statement matching
from re import compile as rec

# file and directory searching
from os import listdir
from os.path import isfile, isdir, join

def analyze(filename):
    """Analyzes a Karel file and outputs warning and errors found.

    Args:
        filename: The path of the file to analyze.
    Returns:
        True if no errors found, False otherwise.
    """

    # make sure file exists
    if not isfile(filename):
        print('Invalid filename "' + filename + '".')
        return
    else:
        print('\nAnalyzing ' + filename + ' for syntax errors...')
        #print('Beginning analysis of "' + filename + '".')

    # set of all available instructions
    # newly defined instructions found in the file will be added to this set
    defined_instructions = set([
        'move', 'turn_left',
        'put_beeper', 'pick_beeper',
        'beepers_present', 'beepers_in_bag',
        'left_is_clear', 'front_is_clear', 'right_is_clear',
        'facing_north', 'facing_east', 'facing_south', 'facing_west'
    ])

    # set of statements that cause indentation
    # these statements also allow same-line statements, cancelling indentation
    indenting_statements = set([
        'if', 'else', 'def', 'while', 'for',
    ])

    # set of functions that need a conditional statement after it
    conditional_statements = set(['if', 'while'])

    # set of functions that return a boolean
    boolean_statements = set([
        'beepers_present', 'beepers_in_bag',
        'left_is_clear', 'front_is_clear', 'right_is_clear',
        'facing_north', 'facing_east', 'facing_south', 'facing_west'
    ])

    # regular expressions for matching

    # line splitting by whitespace
    lineRE = rec(r'\s+')
    # conditional after if, while
    conditionalRE = rec(r'\s*(?:not\s+)*[a-zA-Z_]\w*\s*\(\s*\)\s*$')
    # statement / comment after indenter
    statementRE = rec(r'\s*[a-zA-Z_]\w*\s*\(\s*\)\s*(?:#.*\s*)?$')
    commentRE = rec(r'\s*(?:#.*\s*)?$')
    # instruction definition
    defRE = rec(r'def\s+[a-zA-Z_]\w*\s*\(\s*\)\s*:.*\s*$')
    # for loop
    forRE = rec(r'for\s+[a-zA-Z_]\w*\s+in\s+range\s*\(\s*\d+\s*\)\s*:.*\s*$')
    # else statement
    elseRE = rec(r'else\s*:.*\s*$')
    # karel import
    fromRE = rec(r'from\s+karel\s+import\s*\*\s*(?:#.*\s*)?$')
    # function (instruction) call
    callRE = rec(r'\w+\s*\(\s*\)\s*(?:#.*\s*)?$')

    # flags
    karel_imported = False      # {from karel import *} called
    program_began = False       # {begin_karel_program} called
    program_ended = False       # {end_karel_program} called
    commented = False           # multiline comments
    last_line_indents = False   # last statement was indenting
    indent_levels = []          # indentation depth levels
    depth = 0                   # current indentation level (0 is top level)

    # error logging
    error_list = []

    # preliminary search for instruction definitions
    file = open(filename)
    imported = False
    for line in file:
        # only allow after import and before begin_karel_program
        if not imported:
            if fromRE.fullmatch(line): imported = True
            continue
        if line.startswith('begin_karel_program'): break

        # confirm matching
        if defRE.fullmatch(line):
            # find and add definition name to set
            parts = [x for x in line.partition(':')[0].split(' ') if x]
            name = parts[1].strip('()')
            defined_instructions.add(name)
    file.close()

    # process lines
    file = open(filename)
    tabs_reported = False
    for i, line in enumerate(file):
        def add_error(message):
            """Appends a message to the current line."""
            error_list.append((i, message))

        # remove indent space
        cur_depth = 0
        tabs_used = False
        while line.startswith((' ', '\t')):
            if line.startswith('\t'):
                cur_depth += 3
                tabs_used = True
            line = line[1:]
            cur_depth += 1

        # split line into tokens, ignore empty strings
        tokens = [x for x in lineRE.split(line) if x]
        if not tokens: continue

        # comments: high priority in case of skipping lines
        comments = line.count('"""')
        comment_line = line
        for _ in range(comments):
            commented = not commented # toggle multiline string
            comment_line = comment_line.partition('"""')[2].strip(' \n')
            beginning = comment_line.partition('"""')[0].strip(' \n')
            if not commented and beginning: # something after a multiline
                if not commentRE.fullmatch(beginning): # ignore comments
                    add_error("Error: Unexpected token '" + beginning + "'.")
        if commented or comments or line.startswith('#'):
            continue # commented: skip line processing

        # indentation type error
        if tabs_used and not tabs_reported:
            add_error('Warning: Indented using tabs, consider using spaces.')
            tabs_reported = True

        # indentation depth errors
        if last_line_indents:
            if cur_depth <= depth:
                add_error('Error: Expected indentation.')
        elif not last_line_indents and cur_depth > depth:
            add_error('Error: Unexpected indentation.')
        depth = cur_depth # update depth

        # statement flags

        # update indentation levels
        popped_levels = []
        while indent_levels and indent_levels[-1][0] >= depth:
            popped_levels.append(indent_levels.pop())
        if popped_levels and popped_levels[-1][0] != depth:
            add_error('Error: Unindent misaligned.')

        # non definition calls before begin_karel_program()
        if tokens[0] != 'def':
            calls = [x for x in tokens if x.strip('():') in defined_instructions]
            if not [l for l in indent_levels if l[1] == 'def'] \
            and calls and not program_began:
                add_error('Error: Instruction call before begin_karel_program().')
        # calls after end_karel_program()
        if program_ended:
            add_error('Warning: Statement after end_karel_program().')

        # indenting statement errors
        base = tokens[0].partition(':')[0]
        if base in indenting_statements:
            # check for colon
            parts = line.partition(':')
            if not parts[1]: add_error('Error: Missing ":" in statement.')
            # find and analyze same-line statement if exists
            statement = parts[2]
            # no statements: indent and add to levels
            if commentRE.fullmatch(statement):
                last_line_indents = True
                indent_levels.append((depth, base))
            # statement exists: check validity
            elif statementRE.fullmatch(statement):
                call = _find_statement(tokens)
                if call not in defined_instructions:
                    add_error('Error: Unrecognized instruction "' + call + '".')
                # match with later else
                if base == 'if':
                    indent_levels.append((depth, base))
                last_line_indents = False
            # some error
            else: add_error('Error: Invalid statement "' + statement + '".')
        # not indenting
        else: last_line_indents = False

        # conditional
        if tokens[0] in conditional_statements:
            # conditional statement exists and matches regex
            call = _find_condition(tokens)
            conditional = line[len(tokens[0])+1:].partition(':')[0]
            if not conditionalRE.fullmatch(conditional) \
            or call not in boolean_statements:
                 add_error('Error: Invalid conditional "' + conditional + '".')

        # specific statement processing

        # definition
        if tokens[0] == 'def':
            if not defRE.fullmatch(line):
                add_error('Error: Invalid instruction definition.')
            elif not karel_imported:
                add_error('Error: Instruction definition before karel import.')
            elif program_began:
                add_error('Error: Instruction definition after begin_karel_program.')
            if depth > 0: # extra check
                add_error('Warning: Non-top level definition.')
        # while loop: nothing
        elif tokens[0] == 'while': pass
        # for loop
        elif tokens[0] == 'for':
            if not forRE.fullmatch(line):
                add_error('Error: Invalid for statement.')
        # if statement: nothing
        elif tokens[0] == 'if': pass
        # else statement
        elif tokens[0].partition(':')[0] == 'else':
            if not elseRE.fullmatch(line):
                add_error('Error: Invalid else statement.')
            elif not popped_levels or popped_levels[-1][1] != 'if':
                add_error('Error: else statement without if statement.')
        # one of the instructions
        elif tokens[0].partition('(')[0].strip() in defined_instructions:
            if not callRE.fullmatch(line):
                add_error('Error: Invalid instruction call.')
        # import
        elif tokens[0] == 'from':
            if not fromRE.fullmatch(line):
                add_error('Error: Invalid import.')
            elif karel_imported:
                add_error('Warning: Karel already imported.')
            karel_imported = True
        # begin_karel_program
        elif tokens[0].partition('(')[0].strip() == 'begin_karel_program':
            if not callRE.fullmatch(line):
                add_error('Error: Invalid begin_karel_program().')
            elif not karel_imported:
                add_error('Error: Called begin_karel_program() before import.')
            elif program_began:
                add_error('Error: begin_karel_program() already called.')
            program_began = True
        # end_karel_program
        elif tokens[0].partition('(')[0].strip() == 'end_karel_program':
            if not callRE.fullmatch(line):
                add_error('Error: Invalid end_karel_program().')
            elif program_ended:
                add_error('Error: end_karel_program() already called.')
            if depth != 0:
                add_error('Warning: Nested end_karel_program().')
            else:
                program_ended = True
        # unrecognized
        else:
            add_error('Error: Unrecognized token "' + tokens[0] + '".')

    # done processing
    file.close()

    # global flag errors
    if commented:
        # negative indexes to appear first when sorting errors
        error_list.append((-1, "Warning: Unterminated comment."))
    if not karel_imported:
        error_list.append((-4, "Error: from karel import * not found."))
    if not program_began:
        error_list.append((-3, "Error: begin_karel_program() never called."))
    if not program_ended:
        error_list.append((-2, "Error: end_karel_program() never called."))

    # output errors by line order
    if error_list:
        print('Found ' + str(len(error_list)) + ' possible problem'
              + ('s' if i > 1 else '') + ':')
        # print('Found ' + str(len(error_list)) + ' error'
        #     + ('s ' if i > 1 else ' ') + 'in "' + filename + '".')

        # sort by line number and output
        error_list.sort()
        for line, message in error_list:
            # replace newlines with explicit characters for readability
            if line < 0: print('  Global ' + message.replace('\n', '\\n'))
            else: print('  ' + str(line + 1) + ' - ' + message.replace('\n', '\\n'))

        return False
    else: # nice
        print('No syntax errors detected.')
        return True


def _find_condition(tokens):
    """
    Returns the non-bracket, non-empty condition
    token immediately before the colon, or an empty string
    if there is no colon or the tokens begin with the colon.

    Args:
        tokens: The tokens to search through.
    """
    try:
        # find token with :
        contains = [x for x in enumerate(tokens) if ':' in x[1]][0]
        # loop back to find non bracket item
        if contains[1].startswith(':'):
            for i in range(contains[0]-1, -1, -1):
                contains = tokens[i].strip('():')
                if contains: return contains
        else:
            return contains[1].partition(':')[0].strip('():')
    except:
        return ''

def _find_statement(tokens):
    """
    Returns the non-bracket, non-empty statement
    token immediately after the colon, or an empty string
    if there is no colon or the tokens ends with the colon.

    Args:
        tokens: The tokens to search through.
    """
    try:
        # find token with :
        item = [x for x in enumerate(tokens) if ':' in x[1]][0]

        # get item immediately after
        if item[1].endswith(':'):
            statement = tokens[item[0]+1]
        else:
            statement = item[1].partition(':')[2]

        # account for suffixed comment
        return statement.partition('#')[0].strip('():')
    except:
        return ''

def analyzedir(path=None):
    """Analyze the files in a directory.

    If path is None, the function will search the local directory
    for files to analyze. Note that unlike the analyze() function,
    this function will only accept .py files to analyze, and will
    ignore other file types, such as .txt.

    This function ignores __init__.py files, and will also ignore
    karelanalyzer.py if a local directory search is performed.

    Args:
        path: The directory containing the .py files to analyze.
            Defaults to None.
    """

    # empty string or None path
    if not path:
        print('No directory specified. Searching local directory for files.')
        path = '.'
    elif not isdir(path):
        print('Invalid directory specified.')
        return

    # files to ignore
    ignored_files = set(['__init__.py'])
    if path == '.': # local directory: ignore own file
        ignored_files.add('karelanalyzer.py')

    # find files to analyze
    files = [join(path, f) for f in listdir(path) if isfile(join(path, f))
            and f.endswith('.py') and f not in ignored_files]

    # no files to analyze: return
    if not files:
        print('No valid .py files found at path "' + path + '".')
        return

    # analyze all, alphabetically
    print('Analyzing files at path "' + path + '".\n')
    for file in sorted(files):
        analyze(file)

    print('Finished analyzing directory.')

# if run as main file, import sys and start analysis automatically
if __name__ == '__main__':
    import sys

    # no arguments: analyze local directory
    if len(sys.argv) <= 1:
        analyzedir()
    else:
        # go through given arguments
        for path in sys.argv[1:]:
            # analyze file directly
            if isfile(path): analyze(path)
            # analyze given directory
            elif isdir(path): analyzedir(path)
            # give up, go home
            else: print('Invalid path: ' + path)
