import subprocess
import sys
import os

def run_app():
    """
    Runs the Streamlit app.
    """
    # Detect if we are already running inside a Streamlit script runner
    # This happens if the user mistakenly runs 'streamlit run main.py'
    try:
        from streamlit.runtime.scriptrunner import get_script_run_ctx
        if get_script_run_ctx():
            import streamlit as st
            st.error("## ⚠️ Incorrect Usage Detected\n"
                     "It looks like you ran `streamlit run main.py`.\n\n"
                     "Please run the application using:\n"
                     "```bash\npython main.py\n```")
            st.stop()
            return
    except ImportError:
        pass

    app_path = os.path.join("src", "ui", "app.py")
    if not os.path.exists(app_path):
        print(f"Error: Could not find {app_path}")
        sys.exit(1)

    # Use sys.executable to ensure we use the same Python environment
    # Using -m streamlit run is more robust than calling the 'streamlit' command directly
    cmd = [sys.executable, "-m", "streamlit", "run", app_path]
    
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running Streamlit: {e}")
        sys.exit(e.returncode)
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        pass

if __name__ == "__main__":
    run_app()
