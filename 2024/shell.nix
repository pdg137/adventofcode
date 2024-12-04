let
  # Change to this if you want to use your configured channel
  #  nixpkgs = <nixpkgs>;

  # Otherwise, use nixos-24.11 from 2024-12-03:
  nixpkgs = fetchTarball {
    url = "https://github.com/NixOS/nixpkgs/archive/f9f0d5c.tar.gz";
    sha256 = "1nv2gvdzdqcrzac353yanm432cpbs5x18d9m7h529pj9hm5a0zqj";
  };

  pkgs = (import nixpkgs {});
  gemset = import ./our_gemset.nix pkgs;

in

  pkgs.stdenvNoCC.mkDerivation {
    name = "shell";
    dontUnpack = "true";
    buildInputs = [
      gemset
      gemset.ruby
    ];

    # prevent nixpkgs from being garbage-collected
    inherit nixpkgs;

    builder = builtins.toFile "builder.sh" ''
      source $stdenv/setup
      eval $shellHook

      {
        echo "#!$SHELL"
        for var in PATH SHELL nixpkgs
        do echo "declare -x $var=\"''${!var}\""
        done
        echo "declare -x PS1='\n\033[1;32m[nix-shell:\w]\$\033[0m '"
        echo "exec \"$SHELL\" --norc --noprofile \"\$@\""
      } > "$out"

      chmod a+x "$out"
    '';
  }
