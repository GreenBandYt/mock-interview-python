# 🧰 PowerShell-скрипт: Генерация структуры проекта

Этот скрипт автоматически генерирует древовидную структуру проекта `mock-interview-python`,  
исключая временные, служебные и лишние директории, и сохраняет результат в файл `project_structure.txt`.

---

## 🚀 Как использовать

1. Открой PowerShell в корневой папке проекта:
   ```powershell
   cd F:\ShareFolder\mock-interview-python
   ```

2. Вставь и выполни скрипт вручную — **или сохрани его в `.ps1` файл и запускай при необходимости**.

3. Результат будет сохранён в файл:
   ```
   project_structure.txt
   ```

---

## 📂 Что делает скрипт

- Обходит только важные папки проекта: `api`, `bot`, `core`, `data`, `docs`, `templates`, `tests`
- Показывает только важные файлы: `.py`, `.html`, `.css`, `.js`, `.md`
- Исключает из обхода: `.venv`, `.idea`, `logs`, `migrations`, `secrets`, `__pycache__`, `.git`
- Также добавляет ключевые файлы в корне проекта: `.env.*`, `README.md`, `main.py`, `requirements.txt`

---

## 🧾 Исходный код скрипта

```powershell
$output = @()
$output += "mock-interview-python/"
$dirs = Get-ChildItem -Directory -Exclude ".venv",".idea","logs","migrations","secrets" | Where-Object { $_.Name -notmatch "(__pycache__|\.git)" }
$validDirs = "api","bot","core","data","docs","templates","tests"

foreach ($dir in $dirs) {
    if ($dir.Name -notin $validDirs) { continue }
    $output += "|-- $($dir.Name)/"
    Push-Location $dir.Name

    $files = Get-ChildItem -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -match "\.(py|html|css|js|md)$" }
    foreach ($file in $files) { $output += "|   |-- $($file.Name)" }

    $subdirs = Get-ChildItem -Directory -ErrorAction SilentlyContinue
    foreach ($subdir in $subdirs) {
        $output += "|   |-- $($subdir.Name)/"
        Push-Location $subdir.Name

        $subfiles = Get-ChildItem -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -match "\.(py|html|css|js|md)$" }
        foreach ($subfile in $subfiles) { $output += "|   |   |-- $($subfile.Name)" }

        $subsubdirs = Get-ChildItem -Directory -ErrorAction SilentlyContinue
        foreach ($subsubdir in $subsubdirs) {
            $output += "|   |   |-- $($subsubdir.Name)/"
            Push-Location $subsubdir.Name

            $subsubfiles = Get-ChildItem -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -match "\.(py|html|css|js|md)$" }
            foreach ($subsubfile in $subsubfiles) { $output += "|   |   |   |-- $($subsubfile.Name)" }

            Pop-Location
        }

        Pop-Location
    }

    Pop-Location
}

$validFiles = Get-ChildItem -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -match "^(\.env\.example|\.env\.dev|\.env\.prod|LICENSE|main\.py|README\.md|requirements\.txt|\.gitignore)$" }
foreach ($file in $validFiles) { $output += "|-- $($file.Name)" }

$output | Out-File project_structure.txt
```

---

## 🧠 Советы

- Скрипт можно положить в `scripts/generate_tree.ps1`
- Или подключить к `Makefile`, `pre-commit` или просто запускать вручную
- Markdown-вывод можно вставлять прямо в `README.md` для визуализации структуры проекта

