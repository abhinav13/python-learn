set textwidth=130  " lines longer than 120 columns will be broken
set shiftwidth=4  " operation >> indents 4 columns; << unindents 4 columns
set tabstop=4     " a hard TAB displays as 4 columns
set expandtab     " insert spaces when hitting TABs
set softtabstop=4 " insert/delete 4 spaces when hitting a TAB/BACKSPACE
set shiftround    " round indent to multiple of 'shiftwidth'
set autoindent    " align the new line indent with the previous line
set nocompatible  " dont know what this does
filetype off      " Dont know what this does either

set rtp+=~/.vim/bundle/vundle/
call vundle#rc()

" let Vundle manage Vundle
" required! 
Bundle 'gmarik/vundle'

" The bundles you install will be listed here

filetype plugin indent on

augroup vimrc_autocmds
        autocmd!
        " highlight characters past column 120
        autocmd FileType python highlight Excess ctermbg=green guibg=Black
        autocmd FileType python match Excess /\%130v.*/
        autocmd FileType python set nowrap
augroup END

Bundle 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
" Powerline setup
set guifont=DejaVu\ Sans\ Mono\ for\ Powerline\ 9
set laststatus=2


"Install Fugitive which is a Git Plugin
"This allows you to call git from within vim
Bundle 'tpope/vim-fugitive'

Bundle 'klen/python-mode'

 " Python-mode
 " DeActivate rope. Ignore the key bindings below. We are using jedi-vim
 " " Keys:
 " " K             Show python docs
 " " <Ctrl-Space>  Rope autocomplete
 " " <Ctrl-c>g     Rope goto definition
 " " <Ctrl-c>d     Rope show documentation
 " " <Ctrl-c>f     Rope find occurrences
 " " <Leader>b     Set, unset breakpoint (g:pymode_breakpoint enabled)
 " " [[            Jump on previous class or function (normal, visual, operator modes)
 " " ]]            Jump on next class or function (normal, visual, operator modes)
 " " [M            Jump on previous class or method (normal, visual, operator modes)
 " " ]M            Jump on next class or method (normal, visual, operator modes)
 " let g:pymode_rope = 1 
 "
 " " Documentation
" let g:pymode_doc = 1
 "let g:pymode_doc_key = 'K'
 "
 " "Linting
 "let g:pymode_lint = 1
" let g:pymode_lint_checker = "pyflakes,pep8"
 " " Auto check on save
 "let g:pymode_lint_write = 1
 "
 " Support virtualenv
 " let g:pymode_virtualenv = 1
 
 " Enable breakpoints plugin
 "let g:pymode_breakpoint = 1
 "let g:pymode_breakpoint_key = '<leader>b'
 "
 " syntax highlighting
 "let g:pymode_syntax = 1
 "let g:pymode_syntax_all = 1
" let g:pymode_syntax_indent_errors = g:pymode_syntax_all
 "let g:pymode_syntax_space_errors = g:pymode_syntax_all
 "
 " autofold code
 "let g:pymode_folding =1 

 " automatically change window's cwd to file's dir
 "set autochdir
