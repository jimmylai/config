alias tmux='tmux -2'
alias tt='tmux attach -t '
alias en='. ~/env/bin/activate'

if [ -n "$PS1" ];
then
	PS1='\[\033[1;34m\]\u\[\033[1;33m\]@\[\033[1;30m\]\h\[\033[1;31m\]\[\033[1;34m\] [\w\[\033[1;34m\]]\[\033[1;36m\] >\[\033[0m\]'
	if [ -n "$YROOT_NAME" ]; then
		PS1='\[\033[1;34m\]\u\[\033[1;33m\]@\[\033[1;30m\]\h:\[\033[1;35m\]$YROOT_NAME\[\033[1;34m\] [\w\[\033[1;34m\]]\[\033[1;36m\] >\[\033[0m\]'
		if [ $YROOT_NAME == "web" ]; then
			export R3HOME=$SOURCE_DIR/projects/web/r3
		fi
	fi
fi
