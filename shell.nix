with import <nixpkgs> {};

mkShell {
  buildInputs = [
    python38
    git
    emacs
    ];
  shellHook = ''
    if [ ! -d ./.venv ]; then
       python -m venv .venv
    fi
    source .venv/bin/activate
    export WORKON_HOME=$(realpath .venv)
    pip install --upgrade pip
    pip install -r requirements.txt;
  '';
}
