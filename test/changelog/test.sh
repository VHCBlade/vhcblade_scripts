cp -r initial_changes/ changes/
cp initial_CHANGELOG.md CHANGELOG.md

python3 ../../python/changelog_collate.py

if cmp -s "CHANGELOG.md" "expected_CHANGELOG.md"; then
    echo "Expected Result..."
else
    echo "Files are different. Exiting with an error."
    exit 1
fi