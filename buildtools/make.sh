#!/bin/sh

# helper functions {{{
die(){
  echo "FATAL ERROR: $1"
  exit 1
}
# }}}

# BUILD {{{
tex_build(){
  [ -z "$1" ] && die "no argument passed to build, expected 1"
  cd "./$1"
  lualatex *.tex
  mkdir -vp "../out/$1"
  cp -v *.pdf "../out/$1/"
}
# }}}

# CLEAN {{{
tex_clean(){
  [ -z "$1" ] && die "no argument passed to clean, expected 1"
  cd "./$1"
  ls -a \
    | grep -E '\.(aux|fls|log|pdf|gz|fdb_latexmk|dvi|xdv)$' \
    | xargs -I{} rm -vf {}
}
# }}}

# WATCH {{{
tex_watch(){
  [ -z "$1" ] && die "no argument passed to watch, expected 1"
  cd "./$1"
  while true; do
    file="$(inotifywait -q -e MODIFY --format %w ./*.tex)"
    echo "$file"
    lualatex "$file"
    mkdir -vp "../out/$1"
    cp -v "${file%.*}.pdf" "../out/$1/"
  done
}
# }}}

# make sure we are in the project root
case "$PWD" in
  */buildtools) cd .. ;;
esac

# run command passed
case "$1" in
  build)
    shift
    tex_build "$@"
    ;;
  clean)
    shift
    tex_clean "$@"
    ;;
  watch)
    shift
    tex_watch "$@"
    ;;
  *)
    die "Unknown command: '$1'"
    ;;
esac

