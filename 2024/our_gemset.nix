pkgs:

let

  gemset = import ./build_gemset.nix pkgs {
    # If you update Gemfile.lock, you will need to revise this hash.
    hash = "sha256-FIi01Xp2NaP6t3P3s/SgAB55Z2j73SnOaXw5Iae80vo=";
    gemfile = ./Gemfile;
    lockfile = ./Gemfile.lock;
  };

in

  pkgs.bundlerEnv {
    name = "bundler-env";
    ruby = pkgs.ruby_3_2; # later versions don't work with emacs :(

    gemfile = ./Gemfile;
    lockfile = ./Gemfile.lock;
    gemset = gemset.outPath;
  }
