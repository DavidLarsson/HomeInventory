with import <nixpkgs> {};

let
  pythonEnv = python38.withPackages (ps: [
            ps.numpy
            ps.toolz
            ps.django]);
in mkShell {
  buildInputs = [
    pythonEnv
    ];
}