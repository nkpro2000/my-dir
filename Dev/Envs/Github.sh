# To add functions/aliases/envs related to GitHub.
# Will be run by ~/nk/Setup/Sh/nk-rcfile.sh (by shell rc files)
# like `for nk_rcfile_sc in ~/nk/Dev/Envs/*; do . "$nk_rcfile_sc"; done` .

# shellcheck shell=sh

ghs () { # GitHub Ssh
    # add the ssh used for git temporarily for single git command
    # usage: ghs FILENAME 'COMMAND'
    # for using ~/nk/Dev/.ssh/gh_FILENAME as ssh key file
    # and executing git COMMAND
    remote_url="$(git remote get-url --push origin 2>/dev/null || echo NotInRepo)"
    if test "$remote_url" = "NotInRepo"; then
        echo 'Not in a git repository' >&2
        return 0
    else
        case "$remote_url" in
            'git@github.com:'*)
                ;; # Already using ssh
            'https://github.com/'*)
                remote_url="git@github.com:$(echo "$remote_url" | cut -d'/' -f4-)"
                ;;
            *)
                echo 'Unknown method on remote url' >&2
                echo 'Current url : '"$remote_url"
                echo 'Enter Remote url (ssh method) manually: '
                read -r remote_url
        esac
    fi

    # setting remote url
    git remote set-url --push origin "$remote_url"

    #$ sudo tree ~/nk/Dev/.ssh -p --metafirst
    #[d--x------]  ~/nk/Dev/.ssh
    #[-r--------]  ├── gh_*
    #[-r--------]  └── gh_*.pub

    #TODO read secret $1 in posix standard.

    if test -n "$2"; then
        # shellcheck disable=SC2030 # Setting variable inside subshell (so local) is intentional.
        (export GIT_SSH_COMMAND='ssh -i '"${HOME}/nk/Dev/.ssh/gh_$1"' -o IdentitiesOnly=yes'; echo "$2" | xargs git)
    else
        # shellcheck disable=SC2031 # Setting variable inside subshell is intentional.
        (export GIT_SSH_COMMAND='ssh -i '"${HOME}/nk/Dev/.ssh/gh_$1"' -o IdentitiesOnly=yes'; git push origin master)
    fi
}
