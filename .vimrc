"syntax color
syntax on
set t_Co=256
set background=dark
colorscheme delek
set number

"ignore case when searching
set ic

"hilight all searched keyword
set hlsearch

"highlight cursor line
set cursorline
highlight CursorLine term=NONE cterm=NONE ctermbg=DarkBlue

"pylint auto check python file when saving file
autocmd FileType python compiler pylint
let g:pylint_inline_highlight = 0
let g:pylint_conventions = 0
let g:pylint_warning = 0
let g:pylint_signs = 1

"hilight selected text
hi Visual cterm=NONE ctermbg=Green ctermfg=White

"highlight searched keyword
highlight Search cterm=NONE ctermfg=Green ctermbg=Red

"indent with 4 space
filetype indent plugin on
autocmd FileType python setlocal et sta sw=4 sts=4

"using python template file
if expand("%") =~ ".*_test\.py"
	autocmd BufNewFile *_test.py 0r ~/.vim/template/test.py
elseif expand("%") =~ ".*\.py"
	autocmd BufNewFile *.py 0r ~/.vim/template/production.py
endif

"map shortcuts
map qq :q<CR>
