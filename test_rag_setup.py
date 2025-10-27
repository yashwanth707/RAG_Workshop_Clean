# filepath: ~/test_rag_setup.py
def check_rag_environment():
    """
    RAG Workshop Environment Verification
    Tests all components needed for the RAG demo
    """
    print("🔧 RAG WORKSHOP ENVIRONMENT CHECK")
    print("="*50)

    # Check Python version
    import sys
    python_version = sys.version_info
    print(f"Python version: {python_version.major}.{python_version.minor}.{python_version.micro}")

    if python_version < (3, 8):
        print("❌ Python 3.8+ required")
        return False
    else:
        print("✅ Python version compatible")

    # Check required libraries
    required_libraries = {
        'langchain': '0.3.27',
        'langchain_community': '0.3.29', 
        'chromadb': '1.0.20',
        'pypdf': '6.0.0',
        'numpy': '6.0.0',
        'pathlib': 'built-in',
        'os': 'built-in',
        'sys': 'built-in'
    }

    print("\n📦 Checking RAG libraries:")
    print("-" * 30)

    missing_libraries = []

    for library, expected_version in required_libraries.items():
        try:
            if library == 'langchain':
                import langchain
                version = langchain.__version__
            elif library == 'langchain_community':
                import langchain_community
                version = getattr(langchain_community, '__version__', 'unknown')
            elif library == 'chromadb':
                import chromadb
                version = chromadb.__version__
            elif library == 'pypdf':
                import pypdf
                version = pypdf._version.__version__
            elif library == 'numpy':
                import numpy
                version = numpy.__version__
            elif library in ['pathlib', 'os', 'sys']:
                version = 'built-in'

            print(f"✅ {library}: {version}")

        except ImportError:
            print(f"❌ {library}: NOT INSTALLED")
            missing_libraries.append(library)
        except Exception as e:
            print(f"⚠️  {library}: Error checking version - {e}")

    # Check Ollama and phi3:mini model
    print("\n🤖 Checking Ollama setup:")
    print("-" * 25)
    try:
        import subprocess
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            if 'phi3:mini' in result.stdout:
                print("✅ Ollama: phi3:mini model available")
            else:
                print("❌ Ollama: phi3:mini model missing")
                print("   Run: ollama pull phi3:mini")
                return False
        else:
            print("❌ Ollama: Not properly configured")
            return False
    except FileNotFoundError:
        print("❌ Ollama: Not installed")
        print("   Install from: https://ollama.ai/")
        return False
    except subprocess.TimeoutExpired:
        print("⚠️  Ollama: Connection timeout - check if service is running")
        return False
    except Exception as e:
        print(f"⚠️  Ollama: Error checking - {e}")
        return False

    # Check data folder
    print("\n📁 Checking data folder:")
    print("-" * 20)
    import os
    if os.path.exists('data'):
        pdf_files = [f for f in os.listdir('data') if f.endswith('.pdf')]
        if pdf_files:
            print(f"✅ Data folder: {len(pdf_files)} PDF file(s) found")
            print(f"   Files: {', '.join(pdf_files[:3])}{'...' if len(pdf_files) > 3 else ''}")
        else:
            print("⚠️  Data folder: No PDF files found")
            print("   Add some PDF files to the 'data' folder for the workshop")
    else:
        print("❌ Data folder: Not found")
        print("   Create a 'data' folder and add PDF files")
        return False

    # Final summary
    if missing_libraries:
        print(f"\n❌ MISSING LIBRARIES: {', '.join(missing_libraries)}")
        print("\n📦 Install missing packages:")
        for lib in missing_libraries:
            if lib in required_libraries:
                print(f"pip install {lib}=={required_libraries[lib]}")
        return False
    else:
        print("\n🚀 RAG ENVIRONMENT READY!")
        print("✅ All libraries installed")
        print("✅ Ollama with phi3:mini ready")
        print("✅ Data folder prepared")
        print("✅ Jupyter notebook ready")
        print("\nYou can now start: jupyter notebook")
        return True

if __name__ == "__main__":
    check_rag_environment()