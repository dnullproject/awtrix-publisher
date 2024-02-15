{ pkgs ? import <nixpkgs> {} }:

let
  python = pkgs.python310;
  nodejs = pkgs.nodejs-18_x;
in
pkgs.mkShell {
  buildInputs = [
    pkgs.git
    pkgs.curl
    python
    nodejs
    pkgs.lunarvim
  ];

  shellHook = ''
    echo "{
      \"venvPath\": \"${python}/bin\",
      \"include\": [\".\"]
    }" > pyrightconfig.json
  '';
}
