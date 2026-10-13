# codewars

My attempts at [Codewars](https://www.codewars.com/) kata, written while learning Neovim (no better way to practise the keybindings) and picking up Rust.

Layout: `<language>/<kyu level>/<kata>`. Most files keep my first attempt alongside a shorter "best practice" version I found or worked out afterwards, with notes on what I learnt in the comments.

## Running them

```bash
python3 python/7kyu/reverse-words.py
rustc rust/8kyu/rockpaperscissors.rs -o /tmp/rps && /tmp/rps
```

## What I learnt

- Python has a built-in for most things: `min(..., key=len)`, `sorted(set(...))`, `str()`, generator expressions inside `join` and `sum`. My first attempts were often loops that a one-liner replaces.
- Read the spec and edge cases carefully: double spaces in `reverse-words`, negative inputs in `paperwork`.
- Rust's `match` on tuples (`rockpaperscissors.rs`) and that the last expression is the return value without `return`.

## What I would do better

- Keep the kata description and the test cases next to each solution, and run them with `pytest` or `cargo test` instead of `print`.
- Name files consistently (`snake_case`, no brackets or `->` in file names).
- Keep scratch files out of the repo (an empty `test.py` used to sit in the root).
