# wiki-list-formatter
Formats lists of items for MediaWiki wikis. 

Please note that this presumes the heading is "Primary". this worked for a specific purpose. you may need to customize it for your specific needs. 

# WikiFun Formatter

A simple Python script that transforms plain text outlines into [MediaWiki](https://www.mediawiki.org/wiki/Help:Formatting)-formatted markup.

## 📄 What It Does

This script processes a `.txt` file containing outline-style lists (like "Primary 1", "Primary 2", etc.) and:

- Converts each section heading like `Primary 1` into a MediaWiki section header (`== Primary 1 ==`)
- Converts each item under that heading into a bullet point using MediaWiki link syntax:
  ```
  * [[Item listed]]
  ```
- Capitalizes only the **first word** of each item (lowercases the rest) for consistent wiki formatting

The output is written to a file called `result.txt`.

---

## 🧾 Example Input (`list.txt`)

```
List 1
Item Listed
Another Item Listed

Item
Even Another Item

List 2
Item Listed
Another Item Listed
Item
Even Another Item

List 3
Item Listed
Another Item Listed
Item
Even Another Item
```

---

## 📤 Example Output (`result.txt`)

```
== List 1 ==
* [[Item listed]]
* [[Another item listed]]
* [[Item]]
* [[Even another item]]

== List 2 ==
* [[Item listed]]
* [[Another item listed]]
* [[Item]]
* [[Even another item]]

== List 3 ==
* [[Item listed]]
* [[Another item listed]]
* [[Item]]
* [[Even another item]]
```

---

## ⚙️ How to Use

1. Make sure you have Python installed.
2. Copy and paste the `wikifun.py` script into a `.py` file on your computer.
3. Create a `list.txt` file with your content (like in the example above).
4. Open a terminal or command prompt and run the script:

```bash
python wikifun.py list.txt
```

5. The output will be saved as `result.txt` in the same folder.

---

## 🪶 Notes

- This script doesn’t require any external libraries.
- It’s perfect for creating quick MediaWiki pages from structured lists.
- You can manually copy and paste the script and sample input — no need to clone or pull the repository.

