find ./trainData/*.csv -type f | while IFS= read -r file; do
    echo $file
    python exploreFoG_types.py $file
done