with import <nixpkgs> {};

let
  pythonEnv = python38;
in mkShell {
  buildInputs = [
    pythonEnv
    ];
  shellHook = ''
    if [ -d ./.venv ]; then
      rm -rf ./.venv
    fi
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt;
  '';
}