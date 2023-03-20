alias ll='ls -l'
alias la='ls -A'
alias l='ls -CF'

alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias .....='cd ../../../..'
alias ......='cd ../../../../..'

mkcd () {
    mkdir -p "$1" && cd "$1"
}
