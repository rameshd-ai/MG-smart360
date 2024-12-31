from flask import Flask, render_template, request, jsonify, url_for
import os
import json
import pdfkit
from datetime import datetime

app = Flask(__name__, static_folder='static')  # Initialize Flask with the static folder

# Define paths to the static folders for PDF and JSON data
static_folder_path = os.path.join(app.root_path, 'static')
pdf_data_folder = os.path.join(static_folder_path, 'pdf_data')
json_data_folder = os.path.join(static_folder_path, 'json_data_storage')

# Configure pdfkit (if needed for future functionality)
pdfkit_config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
pdfkit_options = {
    'page-size': 'A4',
    'margin-top': '1mm',
    'margin-right': '1mm',
    'margin-bottom': '1mm',
    'margin-left': '1mm',
    'encoding': "UTF-8",
    'no-outline': None,
    'disable-smart-shrinking': True, 
    'enable-local-file-access': True  # Allows wkhtmltopdf to access local files like images or CSS
}

# Ensure the folder for static files exists
if not os.path.exists(static_folder_path):
    os.makedirs(static_folder_path)

# Ensure the PDF data folder exists
os.makedirs(pdf_data_folder, exist_ok=True)

# Ensure the JSON data folder exists
os.makedirs(json_data_folder, exist_ok=True)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/money-receipt-form')
def moneyReceiptForm():
    return render_template('money-receipt-form.html')


@app.route('/lorry-receipt-form')
def lorryReceiptForm():
    return render_template('lorry-receipt-form.html')



# Invoice route
@app.route('/lorry-receipt')  
def invoice():
    try:
        # Open the JSON file in read mode
        json_filename = os.path.join(static_folder_path, 'consignment_form_data.json')
        if os.path.exists(json_filename):
            with open(json_filename, 'r') as json_file:
                data = json.load(json_file)  # Parse the JSON file into a Python dictionary
        else:
            data = {}  # In case the file doesn't exist, return an empty dictionary
    except Exception as e:
        print(f"Error reading JSON file: {e}")  # Print error message if file reading fails
        data = {}  # Return an empty dictionary in case of error
    
    return render_template('lorry-receipt.html', data=data)  # Pass data to the template

# Invoice route
@app.route('/lorry-receipt-view/<folder>/<json_file>')
def lorry_receipt_view(folder, json_file):
    try:
        # Construct the path to the JSON file
        json_file_path = os.path.join(json_data_folder, folder, json_file)
        
        # Debug: Print the resolved file path
        print(f"Accessing JSON file: {json_file_path}")
        
        # Check if the file exists and read its contents
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)  # Parse the JSON file into a Python dictionary
        else:
            # File doesn't exist, return an empty dictionary and log the issue
            data = {}
            print(f"File not found: {json_file_path}")
    except Exception as e:
        # Print error message if file reading fails
        print(f"Error reading JSON file: {e}")
        data = {}  # Return an empty dictionary in case of error

    # Pass the parsed data to the template
    return render_template('lorry-receipt-view.html', data=data)

@app.route('/lorry-receipt-edit/<folder>/<json_file>')
def lorry_receipt_edit(folder, json_file):
    try:
        # Construct the path to the JSON file
        json_file_path = os.path.join(json_data_folder, folder, json_file)
        
        # Debug: Print the resolved file path
        print(f"Accessing JSON file: {json_file_path}")
        
        # Check if the file exists and read its contents
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)  # Parse the JSON file into a Python dictionary
        else:
            # File doesn't exist, return an empty dictionary and log the issue
            data = {}
            print(f"File not found: {json_file_path}")
    except Exception as e:
        # Print error message if file reading fails
        print(f"Error reading JSON file: {e}")
        data = {}  # Return an empty dictionary in case of error

    # Pass the parsed data to the template
    return render_template('lorry-receipt-edit.html', data=data)



@app.route('/money-receipt-edit/<folder>/<json_file>')
def money_receipt_edit(folder, json_file):
    try:
        # Construct the path to the JSON file
        json_file_path = os.path.join(json_data_folder, folder, json_file)
        
        # Debug: Print the resolved file path
        print(f"Accessing JSON file: {json_file_path}")
        
        # Check if the file exists and read its contents
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)  # Parse the JSON file into a Python dictionary
        else:
            # File doesn't exist, return an empty dictionary and log the issue
            data = {}
            print(f"File not found: {json_file_path}")
    except Exception as e:
        # Print error message if file reading fails
        print(f"Error reading JSON file: {e}")
        data = {}  # Return an empty dictionary in case of error

    # Pass the parsed data to the template
    return render_template('money-receipt-edit.html', data=data)


@app.route('/money-receipt')  
def moneyReceipt():
    try:
        # Open the JSON file in read mode
        json_filename = os.path.join(static_folder_path, 'money_receipt.json')
        if os.path.exists(json_filename):
            with open(json_filename, 'r') as json_file:
                data = json.load(json_file)  # Parse the JSON file into a Python dictionary
        else:
            data = {}  # In case the file doesn't exist, return an empty dictionary
    except Exception as e:
        print(f"Error reading JSON file: {e}")  # Print error message if file reading fails
        data = {}  # Return an empty dictionary in case of error
    
    return render_template('money-receipt.html', data=data)  # Pass data to the template


@app.route('/money-receipt-view/<folder>/<json_file>')
def money_receipt_view(folder, json_file):
    try:
        # Construct the path to the JSON file
        json_file_path = os.path.join(json_data_folder, folder, json_file)
        
        # Debug: Print the resolved file path
        print(f"Accessing JSON file: {json_file_path}")
        
        # Check if the file exists and read its contents
        if os.path.exists(json_file_path):
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)  # Parse the JSON file into a Python dictionary
        else:
            # File doesn't exist, return an empty dictionary and log the issue
            data = {}
            print(f"File not found: {json_file_path}")
    except Exception as e:
        # Print error message if file reading fails
        print(f"Error reading JSON file: {e}")
        data = {}  # Return an empty dictionary in case of error

    # Pass the parsed data to the template
    return render_template('money-receipt-view.html', data=data)



@app.route('/save_lrjson', methods=['POST'])
def save_lrjson():
    try:
        # Get form data
        form_data = request.get_json()

        if not form_data:
            return jsonify({'success': False, 'error': 'No data received'}), 400

        # Validate that 'gcNumber' exists in the form data
        gc_number = form_data.get('goodsDetails', {}).get('gcNumber').strip()
        if not gc_number:
            return jsonify({'success': False, 'error': 'gcNumber is missing in the form data'}), 400

        # Save JSON to file
        json_filename = os.path.join(static_folder_path, 'consignment_form_data.json')
        with open(json_filename, 'w') as json_file:
            json.dump(form_data, json_file, indent=2)

        # Create folder using gcNumber if it doesn't exist
        gc_folder_path = os.path.join(json_data_folder, gc_number)
        os.makedirs(gc_folder_path, exist_ok=True)

        # Generate a timestamped filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        json_storage_filename = os.path.join(gc_folder_path, f'consignment_form_data_{timestamp}.json')

        # Save the JSON data with the timestamped filename
        with open(json_storage_filename, 'w') as json_storage_file:
            json.dump(form_data, json_storage_file, indent=2)

        print(f"Data successfully saved in folder: {gc_folder_path}")
        return jsonify({'success': True}), 200
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500
    



@app.route('/save_lr_edit_json', methods=['POST'])
def save_lr_edit_json():
    try:
        # Get form data
        form_data = request.get_json()

        if not form_data:
            return jsonify({'success': False, 'error': 'No data received'}), 400

        # Validate that 'gcNumber' exists in the form data
        gc_number = form_data.get('goodsDetails', {}).get('gcNumber').strip()
        if not gc_number:
            return jsonify({'success': False, 'error': 'gcNumber is missing in the form data'}), 400

        # Save JSON to file
        json_filename = os.path.join(static_folder_path, 'consignment_form_data.json')
        with open(json_filename, 'w') as json_file:
            json.dump(form_data, json_file, indent=2)

        # Create folder using gcNumber if it doesn't exist
        gc_folder_path = os.path.join(json_data_folder, gc_number)
        os.makedirs(gc_folder_path, exist_ok=True)

        # Delete any existing files that start with 'consignment_form_data_' in the folder
        for filename in os.listdir(gc_folder_path):
            if filename.startswith('consignment_form_data_'):
                file_path = os.path.join(gc_folder_path, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted existing file: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")

        # Generate a timestamped filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        json_storage_filename = os.path.join(gc_folder_path, f'consignment_form_data_{timestamp}.json')

        # Save the JSON data with the timestamped filename
        with open(json_storage_filename, 'w') as json_storage_file:
            json.dump(form_data, json_storage_file, indent=2)

        print(f"Data successfully saved in folder: {gc_folder_path}")
        return jsonify({'success': True}), 200
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500
    


@app.route('/save_money_receipt_json', methods=['POST'])
def save_money_receipt_json():
    try:
        # Get form data
        form_data = request.get_json()

        if not form_data:
            return jsonify({'success': False, 'error': 'No data received'}), 400

        # Validate that 'gcNumber' exists in the form data
        gc_number = form_data.get('gcNumber').strip()
        if not gc_number:
            return jsonify({'success': False, 'error': 'gcNumber is missing in the form data'}), 400

        # Save JSON to file
        json_filename = os.path.join(static_folder_path, 'money_receipt.json')
        with open(json_filename, 'w') as json_file:
            json.dump(form_data, json_file, indent=2)

        # Create folder using gcNumber if it doesn't exist
        gc_folder_path = os.path.join(json_data_folder, gc_number)
        os.makedirs(gc_folder_path, exist_ok=True)

        # Generate a timestamped filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        json_storage_filename = os.path.join(gc_folder_path, f'money_receipt_form_data_{timestamp}.json')

        # Save the JSON data with the timestamped filename
        with open(json_storage_filename, 'w') as json_storage_file:
            json.dump(form_data, json_storage_file, indent=2)

        print(f"Data successfully saved in folder: {gc_folder_path}")
        return jsonify({'success': True}), 200
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500
    
@app.route('/edit_money_receipt_json', methods=['POST'])
def edit_money_receipt_json():
    try:
        # Get form data
        form_data = request.get_json()

        if not form_data:
            return jsonify({'success': False, 'error': 'No data received'}), 400

        # Validate that 'gcNumber' exists in the form data
        gc_number = form_data.get('gcNumber').strip()
        if not gc_number:
            return jsonify({'success': False, 'error': 'gcNumber is missing in the form data'}), 400

        # Save JSON to file
        json_filename = os.path.join(static_folder_path, 'money_receipt.json')
        with open(json_filename, 'w') as json_file:
            json.dump(form_data, json_file, indent=2)

        # Create folder using gcNumber if it doesn't exist
        gc_folder_path = os.path.join(json_data_folder, gc_number)
        os.makedirs(gc_folder_path, exist_ok=True)

        # Delete any existing files that start with 'consignment_form_data_' in the folder
        for filename in os.listdir(gc_folder_path):
            if filename.startswith('money_receipt_form_data_'):
                file_path = os.path.join(gc_folder_path, filename)
                try:
                    os.remove(file_path)
                    print(f"Deleted existing file: {file_path}")
                except Exception as e:
                    print(f"Error deleting file {file_path}: {e}")


        # Generate a timestamped filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        json_storage_filename = os.path.join(gc_folder_path, f'money_receipt_form_data_{timestamp}.json')

        # Save the JSON data with the timestamped filename
        with open(json_storage_filename, 'w') as json_storage_file:
            json.dump(form_data, json_storage_file, indent=2)

        print(f"Data successfully saved in folder: {gc_folder_path}")
        return jsonify({'success': True}), 200
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500
    


@app.route('/lorry-receipt-list')
def invoice_list():
    return render_template('lorry-receipt-list.html')

@app.route('/money-receipt-list')
def money_receipt_list():
    return render_template('money-receipt-list.html')

@app.route('/lr_list', methods=['GET'])
def lr_list():
    try:
        # Get JSON files in subfolders recursively
        def get_json_files(directory):
            folder_data = []
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isdir(item_path):  # If it's a subfolder
                    folder_info = {
                        'folder_name': item,
                        'json_files': []  # This will hold JSON files for this folder
                    }
                    # Recursively get JSON files inside the subfolder
                    for sub_item in os.listdir(item_path):
                        sub_item_path = os.path.join(item_path, sub_item)
                        if os.path.isfile(sub_item_path) and sub_item.endswith('.json') and sub_item.startswith('consignment_form_data'):
                            folder_info['json_files'].append(sub_item)
                    # If the folder has JSON files, add it to the list
                    if folder_info['json_files']:
                        folder_data.append(folder_info)
            return folder_data

        # Fetch the JSON file structure
        folder_data = get_json_files(json_data_folder)

        return jsonify(folder_data)  # Return the folder structure as JSON
    except Exception as e:
        print(f"Error fetching JSON files: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500
    


@app.route('/mr_list', methods=['GET'])
def mr_list():
    try:
        # Get JSON files in subfolders recursively
        def get_json_files(directory):
            folder_data = []
            for item in os.listdir(directory):
                item_path = os.path.join(directory, item)
                if os.path.isdir(item_path):  # If it's a subfolder
                    folder_info = {
                        'folder_name': item,
                        'json_files': []  # This will hold JSON files for this folder
                    }
                    # Recursively get JSON files inside the subfolder
                    for sub_item in os.listdir(item_path):
                        sub_item_path = os.path.join(item_path, sub_item)
                        if os.path.isfile(sub_item_path) and sub_item.endswith('.json') and sub_item.startswith('money_receipt_form_data'):
                            folder_info['json_files'].append(sub_item)
                    # If the folder has JSON files, add it to the list
                    if folder_info['json_files']:
                        folder_data.append(folder_info)
            return folder_data

        # Fetch the JSON file structure
        folder_data = get_json_files(json_data_folder)

        return jsonify(folder_data)  # Return the folder structure as JSON
    except Exception as e:
        print(f"Error fetching JSON files: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
