a = "⌘ ✲ ⎈ ^ ⌃ ❖ ⎇ ⌥ ⇮ ◆ ◇ ✦ ✧ ⇧ ⇪ 🄰 🅰 ⇪ ⇬ ⇭ ↩ ↵ ⏎ ⌤ ⎆ ▤ ☰ 𝌆 ⎄ ⭾ ↹ ⇄ ⇤ ⇥ ↤ ↦ ⎋ ⌫ ⟵ ⌦ ⎀ ⎚ ⌧ ↖ ↘ ⇤ ⇥ ⤒ ⤓ ⇞ ⇟ △ ▽ ▲ ▼ ⎗ ⎘ ↑ ↓ ← → ◀ ▶ ▲ ▼ ◁ ▷ △ ▽ ⇦ ⇨ ⇧ ⇩ ⬅ ➡ ⬆ ⬇ ⎉ ⎊ ⎙ ⍰ ℹ 🛈 ☾ ⏏ ✉ ⌂ ✂ ✄ ⎌ ↶ ↷ ⟲ ⟳ ↺ ↻ 🕨 🕩 🕪 ◼ ⏯ ⏮ ⏭ ✗ ⌖ ⯐ ♼ ♽ ♺ ♳ ♴ ♵"
new_a=''
lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
for i in range(len(a)):
    if i%len(lorem) == 0:
        new_a+="\n"
    new_a+=a[i]
print(new_a)