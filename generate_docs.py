import os
import subprocess

# 모듈 정보
modules = [
    "binance_api",
    "data_manager",
    "main",
    "models",
    "trading",
    "utils",
]
modules_dir = "src/"
output_dir = "docs"

# 각 모듈에 대한 문서 생성
for module in modules:
    module_path = modules_dir + module
    subprocess.run(
        ["pdoc", "--html", module_path, "--output-dir", output_dir, "--force"],
        check=True,
    )

# index.html 파일 생성
index_content = """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Trading Docs</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 20px;
            background-color: #f4f4f4;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        h1 {
            text-align: center;
            color: #000000;
        }
        ul {
            list-style: none;
            padding: 0;
        }
        li {
            margin: 10px 0;
            padding: 10px;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        a {
            color: #0275d8;
            text-decoration: none;
            font-weight: bold;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
<div class="container">
    <h1>Project Documentation</h1>
    <ul>"""

for module in modules:
    module_path = os.path.join(module, "index.html")
    index_content += f'<li><a href="{module_path}">{module}</a></li>'

index_content += """
    </ul>
</div>
</body>
</html>"""

with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_content)
