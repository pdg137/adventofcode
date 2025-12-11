let
  # Change to this if you want to use your configured channel
  #  nixpkgs = <nixpkgs>;

  # nixos-25.11 from 2025-11-30:
  nixpkgs-version = "d542db7";
  nixpkgs = fetchTarball {
    name = "nixpkgs-${nixpkgs-version}";
    url = "https://github.com/NixOS/nixpkgs/archive/${nixpkgs-version}.tar.gz";
    sha256 = "0x6wjmpzxrrlmwwq8v3znpyr1qs5m1vf9bdgwwlq0lr5fl8l4v67";
  };

  pkgs = import nixpkgs {};

  gwbasic = pkgs.fetchzip {
    url = "https://web.archive.org/web/20091027064135/http://www.geocities.com/KindlyRat/GWBASIC.EXE.zip";
    sha256 = "sha256-aN+xJ9FA897fI0O1ZtZ/Ih/0O2Ze1BmtWudH3pIkH2o=";
  };

in

  pkgs.stdenvNoCC.mkDerivation {
    name = "shell";
    dontUnpack = "true";
    buildInputs = [
      pkgs.emacs-nox
      pkgs.php
      pkgs.octave
      pkgs.dosbox-x # for running GW-BASIC
      pkgs.texliveMinimal
      pkgs.tcl-9_0
    ];

    # prevent nixpkgs from being garbage-collected
    inherit nixpkgs;

    inherit gwbasic;

    builder = builtins.toFile "builder.sh" ''
      source $stdenv/setup
      eval $shellHook

      {
        echo "#!$SHELL"
        for var in PATH SHELL nixpkgs gwbasic
        do echo "declare -x $var=\"''${!var}\""
        done
        echo "declare -x PS1='\n\033[1;32m[nix-shell:\w]\$\033[0m '"
        echo "exec \"$SHELL\" --norc --noprofile \"\$@\""
      } > "$out"

      chmod a+x "$out"
    '';
  }
