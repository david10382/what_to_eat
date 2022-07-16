if [[ $# -eq 1 ]]; then
    echo "There are parameters"
    if [[ "$1" == "run" ]]; then
        echo "Start main_app.py"
        python3 main_app.py
    fi
    
else 
    echo "No parameter"
fi
