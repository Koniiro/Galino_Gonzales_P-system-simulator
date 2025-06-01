{ pkgs ? import <nixpkgs> {} }:
let
  python = (
    (import (builtins.fetchTarball {
      url = "https://github.com/NixOS/nixpkgs/archive/12a55407652e04dcf2309436eb06fef0d3713ef3.tar.gz";
    }) {}).python310
  );
in
pkgs.mkShell {
  buildInputs = [
    python
    pkgs.zlib
  ];
  nativeBuildInputs = [
  ];
  shellHook = ''
             # blah blah blah
         '';
  LD_LIBRARY_PATH = "${pkgs.zlib}/lib:${pkgs.stdenv.cc.cc.lib}/lib";
}
