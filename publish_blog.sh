#!/bin/bash
echo "==============================="
echo "🚀 Publishing Blog to GitHub..."
echo "==============================="

cd /c/Projects/multi-agent-blog || exit

git add .
git commit -m "🔄 Update blog index.html and images"
git push origin main

echo "==============================="
echo "✅ Blog Pushed Successfully!"
echo "==============================="
