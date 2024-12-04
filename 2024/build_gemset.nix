pkgs:
{ hash, gemfile, lockfile }:

let
  hashDrvInputs = drv:
    let
      inputs = { inherit (drv) builder args buildInputs gemfile lockfile; };
      json = builtins.toJSON inputs;
    in
      builtins.hashString "md5" json;

  uniqueGemsetName = "${hashDrvInputs gemset}-gemset.nix";

  gemset = pkgs.stdenv.mkDerivation {
    name = uniqueGemsetName;

    gemfile = gemfile;
    lockfile = lockfile;

    # Make it a fixed-output derivation to allow Internet downloads.
    outputHashMode = "flat";
    outputHashAlgo = "sha256";
    outputHash = hash;

    buildInputs = [ pkgs.cacert pkgs.bundix pkgs.nix pkgs.openssl ];

    # To build gemset.nix we need nix-prefetch-url, which fails in
    # nix-build since it can't write to /var/nix.  So we create a fake
    # directory for it.
    builder = pkgs.writeShellScript "builder.sh" ''
      source $stdenv/setup
      export XDG_CACHE_HOME="$PWD"

      mkdir fake_nix
      export NIX_STORE_DIR="$PWD"/fake_nix/store
      export NIX_STATE_DIR="$PWD"/fake_nix/var/nix
      export NIX_LOG_DIR="$PWD"/fake_nix/var/log/nix

      bundix --lockfile=$lockfile --gemfile=$gemfile --gemset=$out
    '';
  };
in
  gemset
