# import time
# import requests
# import base64
# import json
# import smtplib
# import os
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.image import MIMEImage

# # --- AUTOMATION CONFIGURATION PARAMETERS ---
# DROPBOX_TOKEN = "sl.u.AGiE2jzClBVzhTDUvLW32-VRtlCyURyMyQaJNjq4aijP90aRMXb5tdtTk7KCHcwvwoQcV5licvvcpmZX4yrs1hwYSeRHaPPDPrif309XnUKQmrUJTWF9te2Uz17Lr4QO1MU-WncAvsztPCywEf-uZzty2tgrOINvmdc6ntdmYepJ2Pca52mDQmGEvOP-sZU9T3klNAf4dDr0gVXnnvUl9Gcc-KLh_zvJSshwWKgGPYMHQn_c3tTA79YlFkWujvchHKSQ1BgtHCoQUSm78bf__qdW11pvsGWFTPlnYSYddsS-KmKh1n6cBIG1pW8_q9UPlBYY_rvVV9nzm8wgDGFBumZwZVHaAXzVJOSSSAxZRyR1CMO9UbaHPTq7xa1nSOSBcvXxuziTHHjres4yibgxDaTjzBQyjeVUIDaYyyZ7LMBQTu1Ck4Hp2J_aS-z-UXV4j7dBkXPlH3yDBUUxyjGklcZba0HcKzqV8qPOVGvo0UbQu5XrcYeGDW-aLg2jS0AnYGXsOXdw5ZI2PWNPcNi3MLx1v769zPQ8XQtjJ606cano-GWG1GimIJKuTUNeg7lkViJRpNlJZz7r6qruHxeWP6mkFBkG-tlP5Mujj_RxeXgZzlBtLY0zWpgBJi4WQ62ombLLQI8nx7YM1sXFiTcZlIrfQFp0qeL9AqgqXgdZdvYYlc5e0Z3dQLVFYtgluEQp3EkyM9wptmF0ZbDNvhc6ZZIlbFt_kDsTwOsHkQXnAlAUeF7QwA-s-WjjuVPuzeYj9RrZ0BN9ATsW83fdL5JjYUCzQu5zR44fJ4cynmbO-0TIe0OZMz1L9W5dtmv8HDyREKUTXAH3QAspUljUV4fBYOQItpw0TQwFd2NIJKe_enwjT8ZQET3SiLu97iVNqZVc_VftE5179WoRZCq0s9RrAApDSvhEH3uS0lnVnFpf3VIaHvy3VQ2kxGXSZKYMJ6n31G4VzaCWRysqVwBERkY98SDw6GHbYAot0bSfYnDhOIgabdkaN-Qh2AsL74q7m5kNj4ijJQt2h11zimJToFDr2w4KthXoqvkO6qOl4P6hOj6eed3LVFV6REqEwfoFJkUYb4M4SQrTWnT0aDxNSz54a6IbZfsBJUmpzXwv9cXbbUY45bf6x2V-UnNPx11vgHhS-vjJXL7w1EMxycz4A9IvZjxLrqyqPbVFu4xCQS5kZqwVGEjYbS1kJhmGDETmhZcc3J5Kpo_4wvujfyZcWhYq-rh5QeGc3hGjdf40CjYDWgfA-IxYXDvsPppmydxMZ-z1kN1oPM3mRBCt4iV4s9l-wm4N4Dvumn_Smg_nyW-OpjAsnp_UuqVV9OnW1hd9swr0O8mixELvbxWpSbJ9sVp-Vi5xjlics9JsOd54cEwXfs04KbmIGdDJ8vU9k-nKOqUecQ0Cxdh1rk4JAvGvvecZmHX2yvD62L18mE5WgqDYHY29CFyj0lkTgXf5yVr3hI1AJ1c"
# LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
# TARGET_EMAIL = "rdalvi@arcresources.com"

# # --- SYSTEM OUTBOUND EMAIL PARAMS (Option B Authenticated Configuration) ---
# SMTP_SERVER = "smtp.gmail.com"  # e.g., smtp.gmail.com or smtp.office365.com
# SMTP_PORT = 587                     # Standard STARTTLS Port
# SENDER_EMAIL = "jamesthemarksman@gmail.com"
# SENDER_PASSWORD = "hzshpgdrobxzspux"  # Use generated App Password

# # Specialized Operational Inference System Prompts
# PROFILE_PROMPTS = {
#     "gauge": (
#         "You are an on-site pipeline telemetry extraction model. Analyze the provided image. Generate an analysis summary. There may or may not be text. Be detailed in describing what you see. If these are present, focus on and inspect the analogue dials or gauges carefully. If these are not present, describe the image context in its own key and indicate that gauges and dials are not visible in another key. Output strict JSON with schema: { \"asset_id\": \"Unknown/Extract if visible\", \"critical_reading\": \"Value and unit (e.g., 450 PSI)\", \"safety_status\": \"NORMAL/ALERT/CRITICAL based on red lines\", \"ocr_log\": \"Any text stamped on gauge face\", \"image_context\": \"Description of image context if gauges are not visible\", \"gauge_visibility\": \"YES/NO\" }"
#     ),
#     "asset_tag": (
#         "You are an industrial inventory asset management assistant. Analyze the provided image. Generate an analysis summary. There may or may not be text. Be detailed in describing what you see. If these are present, focus on and extract equipment data from nameplates or metal stamps. If these are not present, describe the image context in its own key and indicate that nameplates and metal stamps are not visible in another key. Output strict JSON with schema: { \"asset_id\": \"Serial or Tag tracking code matching site specifications\", \"critical_reading\": \"Manufacturer name and model blueprint number\", \"safety_status\": \"VERIFIED\", \"ocr_log\": \"Complete text block transcription extracted word-for-word\", \"image_context\": \"Description of image context if nameplates or metal stamps are not visible\", \"nameplate_visibility\": \"YES/NO\" }"
#     ),
#     "hazard": (
#         "You are an operational process plant integrity safety inspector. Analyze the provided image. Generate an analysis summary. There may or may not be text. Be detailed in describing what you see. If these are present, focus on and look for environmental degradation, physical damage, rust, or leaks. If these are not present, describe the image context in its own key and indicate that hazards are not visible in another key. Output strict JSON with schema: { \"asset_id\": \"Equipment descriptor matching field site\", \"critical_reading\": \"Specific issue identified (e.g., severe localized pitting corrosion)\", \"safety_status\": \"ACTION REQUIRED/STABLE/HAZARDOUS\", \"ocr_log\": \"All markings or valve designation tags visible in context\", \"image_context\": \"Description of image context if hazards are not visible\", \"hazard_visibility\": \"YES/NO\" }"
#     )
# }

# def list_dropbox_queue():
#     url = "https://api.dropboxapi.com/2/files/list_folder"
#     headers = {
#         "Authorization": f"Bearer {DROPBOX_TOKEN}",
#         "Content-Type": "application/json"
#     }
#     data = {"path": "/field_incoming", "recursive": False}
#     try:
#         res = requests.post(url, headers=headers, json=data)
#         if res.status_code == 200:
#             return res.json().get('entries', [])
#         elif res.status_code == 409:
#             # Path not found: Create directory automatically
#             create_url = "https://api.dropboxapi.com/2/files/create_folder_v2"
#             requests.post(create_url, headers=headers, json={"path": "/field_incoming"})
#         return []
#     except Exception as e:
#         print(f"Network error reading directory listing: {e}")
#         return []

# def download_and_purge_cloud_file(dropbox_path):
#     # Retrieve binary payload
#     down_url = "https://content.dropboxapi.com/2/files/download"
#     headers_download = {
#         "Authorization": f"Bearer {DROPBOX_TOKEN}",
#         "Dropbox-API-Arg": json.dumps({"path": dropbox_path})
#     }
#     file_res = requests.post(down_url, headers=headers_download)
#     file_bytes = file_res.content

#     # Erase data from input queue path to enforce FIFO pipeline locks
#     del_url = "https://api.dropboxapi.com/2/files/delete_v2"
#     headers_api = {"Authorization": f"Bearer {DROPBOX_TOKEN}", "Content-Type": "application/json"}
#     requests.post(del_url, headers=headers_api, json={"path": dropbox_path})
    
#     return file_bytes

# def run_local_vllm_inference(image_bytes, profile_type):
#     base64_str = base64.b64encode(image_bytes).decode('utf-8')
#     data_url = f"data:image/jpeg;base64,{base64_str}"
    
#     system_prompt = PROFILE_PROMPTS.get(profile_type, PROFILE_PROMPTS["gauge"])
    
#     payload = {
#         "model": "loaded-model",
#         "messages": [
#             {"role": "system", "content": system_prompt},
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text", "text": "Extract data from this field image into the requested schema structure. Only return clean JSON code."},
#                     {"type": "image_url", "image_url": {"url": data_url}}
#                 ]
#             }
#         ],
#         "temperature": 0.0
#     }
    
#     res = requests.post(LM_STUDIO_URL, json=payload)
#     res.raise_for_status()
#     raw_text = res.json()['choices'][0]['message']['content']
    
#     # Strip clean json wrapper layers
#     return raw_text.replace("```json", "").replace("```", "").strip()

# def route_engineering_report(json_payload, image_bytes, filename):
#     print(f"Initiating secure email sync to {TARGET_EMAIL} via {SMTP_SERVER}...")
    
#     msg = MIMEMultipart()
#     msg['From'] = SENDER_EMAIL
#     msg['To'] = TARGET_EMAIL
#     msg['Subject'] = f"Automated Telemetry Integration Report - {filename}"

#     msg.attach(MIMEText(f"Processed Machine Analytics Struct:\n\n{json_payload}", 'plain'))
    
#     image_attachment = MIMEImage(image_bytes, name=filename)
#     msg.attach(image_attachment)

#     # Establish an encrypted TLS socket session to securely pass credentials
#     with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
#         server.starttls()  # Upgrade connection to secure TLS encryption
#         server.login(SENDER_EMAIL, SENDER_PASSWORD)
#         server.sendmail(SENDER_EMAIL, TARGET_EMAIL, msg.as_string())

# def execute_polling_loop():
#     print("Cloud Processing Integration Matrix Active.")
#     print("Polling Dropbox directory '/field_incoming' at 10-second intervals...")
    
#     while True:
#         try:
#             entries = list_dropbox_queue()
#             for entry in entries:
#                 if entry['.tag'] == 'file':
#                     dbx_path = entry['path_lower']
#                     filename = entry['name']
#                     print(f"File discovered in intake pipeline: {filename}")
                    
#                     # Identify task profile mapping
#                     profile_type = "gauge"
#                     if "__" in filename:
#                         profile_type = filename.split("__")[0]

#                     # Download and remove from queue
#                     img_bytes = download_and_purge_cloud_file(dbx_path)
                    
#                     # Compute inference on local machine hardware
#                     parsed_json = run_local_vllm_inference(img_bytes, profile_type)
#                     print("Local extraction pass successful.")
                    
#                     print(f"Extracted JSON:\n{parsed_json}\n")

#                     # Dispatch analytical payload to endpoint
#                     route_engineering_report(parsed_json, img_bytes, filename)
#                     print(f"Data packet transmission complete for {filename}.\n")
                    
#         except Exception as e:
#             print(f"Execution processing cycle fault: {e}")
            
#         time.sleep(10)

# if __name__ == "__main__":
#     execute_polling_loop()





import time
import requests
import base64
import json
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# --- AUTOMATION CONFIGURATION PARAMETERS ---
DROPBOX_TOKEN = "sl.u.AGjijCBiKiY3dqGfiaJ0WE2kC66mV0B3ukmxW_ZHiVNjgE2YeY7i4cAmf03odrPMl3b9U2jUg7xCSh5Z4t4suTgINz0N-VoKiMSFV41xRehuVwqYHScwkRNq3fepu9Ut9gyG-Szt8qnD98vF9nkt97ed9e02wg66Ir4Lm_sEy6pSVu31fNVwnUZYEXk-W6uZta006-2yUfr-VbcNI2zuoaTXhwQ8XOOSQxUGN7gf27WIS8N_LYyB_Dz3-bUWnVfKsAFUdqKwswgZMpGtF_51jH-_X3PKfOq-2y6EA-Wb7pBkPAMhTWjRQ5EnxgnuQEEln3wLWEXf1FHKabmsYZss2j2d6F4kzqcf8tP_2vQwrbAG9OjpoyBykbK7_L3Yj1EPlnv8NGW9fga2lS1K5RyI29JBBdLnNVWKWqD_tC7tcDlQz_hR9DNU9qNR21DSwV53y8TEuqaitq4v1Cj7McX0Al3joPSJrTiRI8dzw_oZsqWhLb25VfKAWl7Dafh6yvqiYqn60TY7o3CM19lVOLbC37J2lnxLzQcPV0IQ7WZwBJrE4sj9j_f3ufRPECxAQWSUJtl13C8Wuh8XeTfZ-yRRc6eptX69BpXts2kQSHuP4hnWbfWdH0BUUQJOPHP_lYgQt4foQyPhPyBX_QFXm8D8hkNDEoKUlEbdEvaFXv5JKVCefUfkwPWdxKQkVJdSem2uu5q87Df-MhjoCOEQX8ZCBsO4-o_2pU2WCRwv-ot42pul-bLg47CcA1lG_lOSmoaU5Tq7k_OBmvLMP1XFWxaMCHdfyj9mwaEjP6HWZ783PJHSjPTe_5yA028YnipvTWwq5bemg1yqirhSWTsidBey3oYekeoGWQl1ncxjvxHjJ6LtVP1H5H3evL9W5N-Qwhgt723NntY-XDpEItX1wJ0WOfw30wTomWK3MQPo-roVgn3rHI0qN6O-YgvOZgNHusky5y1KHPAUABAYsJ0WY1OlHj4vQxpewMDOgBHyuLxdRJ7jLkgQrR2mxqk_bQxQJ2ahTncvpiG58XVd8ZyPUYORau-lUa2OP_UHxKjwlp4jsuv7rN-RNfVfBuc0LCqO8TEUTxRtG7O7DzA-MJSFM9rLJUR4hqYsKJpmO0W9eQPazmWOhQT1TM8Z5AfsSL4K20roR_cVTOVB15tlNw7PRgf3BHRvl-iSl-fjDDiEPXxcqJouFxLtrMY1b3WEAMf5I-Rwg-CaX7Pq1HTeTqBQbBIxFeeGW0daj8haCJj3G71qBafpcnoLIwjCtI6A85avFbTzm8A78i1YZkS0mzcQSPNKolSIdnl0ZBQx27SdU_NLbjSMhf93eD0m9VQr_zeUfZHXrIlTzltdcuz2UyTsFz5zMlrytjrUkwtPQINwO2__fTTPnajcd_gyehJtOR9wwoVshkyD6EWFUV15YGXE7q1ZtIyxqmy1VTg6uBFKFVJHsxcwpdQ2oQEklnqO9Kh_-Wirk_w"
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
TARGET_EMAIL = "rdalvi@arcresources.com"

# --- SYSTEM OUTBOUND EMAIL PARAMS (Option B Authenticated Configuration) ---
SMTP_SERVER = "smtp.gmail.com"  # e.g., smtp.gmail.com or smtp.office365.com
SMTP_PORT = 587                     # Standard STARTTLS Port
SENDER_EMAIL = "jamesthemarksman@gmail.com"
SENDER_PASSWORD = "hzshpgdrobxzspux"  # Use generated App Password

# Specialized Operational Inference System Prompts
PROFILE_PROMPTS = {
    "gauge": (
        "You are an on-site pipeline telemetry extraction model. Analyze the provided image. Generate an analysis summary. There may or may not be text. Be detailed in describing what you see. If these are present, focus on and inspect the analogue dials or gauges carefully. If these are not present, describe the image context in its own key and indicate that gauges and dials are not visible in another key. Output strict JSON with schema: { \"asset_id\": \"Unknown/Extract if visible\", \"critical_reading\": \"Value and unit (e.g., 450 PSI)\", \"safety_status\": \"NORMAL/ALERT/CRITICAL based on red lines\", \"ocr_log\": \"Any text stamped on gauge face\", \"image_context\": \"Description of image context if gauges are not visible\", \"gauge_visibility\": \"YES/NO\" }"
    ),
    "asset_tag": (
        "You are an industrial inventory asset management assistant. Analyze the provided image. Generate an analysis summary. There may or may not be text. Be detailed in describing what you see. If these are present, focus on and extract equipment data from nameplates or metal stamps. If these are not present, describe the image context in its own key and indicate that nameplates and metal stamps are not visible in another key. Output strict JSON with schema: { \"asset_id\": \"Serial or Tag tracking code matching site specifications\", \"critical_reading\": \"Manufacturer name and model blueprint number\", \"safety_status\": \"VERIFIED\", \"ocr_log\": \"Complete text block transcription extracted word-for-word\", \"image_context\": \"Description of image context if nameplates or metal stamps are not visible\", \"nameplate_visibility\": \"YES/NO\" }"
    ),
    "hazard": (
        "You are an operational process plant integrity safety inspector. Analyze the provided image. Generate an analysis summary. There may or may not be text. Be detailed in describing what you see. If these are present, focus on and look for environmental degradation, physical damage, rust, or leaks. If these are not present, describe the image context in its own key and indicate that hazards are not visible in another key. Output strict JSON with schema: { \"asset_id\": \"Equipment descriptor matching field site\", \"critical_reading\": \"Specific issue identified (e.g., severe localized pitting corrosion)\", \"safety_status\": \"ACTION REQUIRED/STABLE/HAZARDOUS\", \"ocr_log\": \"All markings or valve designation tags visible in context\", \"image_context\": \"Description of image context if hazards are not visible\", \"hazard_visibility\": \"YES/NO\" }"
    )
}

def list_dropbox_queue():
    url = "https://api.dropboxapi.com/2/files/list_folder"
    headers = {"Authorization": f"Bearer {DROPBOX_TOKEN}", "Content-Type": "application/json"}
    try:
        res = requests.post(url, headers=headers, json={"path": "/field_incoming", "recursive": False})
        if res.status_code == 200:
            return res.json().get('entries', [])
        elif res.status_code == 409:
            # Create root path directories if they don't exist
            requests.post("https://api.dropboxapi.com/2/files/create_folder_v2", headers=headers, json={"path": "/field_incoming"})
            requests.post("https://api.dropboxapi.com/2/files/create_folder_v2", headers=headers, json={"path": "/field_outgoing"})
        return []
    except Exception as e:
        print(f"Network listing error: {e}")
        return []

def download_and_purge_cloud_file(dropbox_path):
    headers_download = {"Authorization": f"Bearer {DROPBOX_TOKEN}", "Dropbox-API-Arg": json.dumps({"path": dropbox_path})}
    file_res = requests.post("https://content.dropboxapi.com/2/files/download", headers=headers_download)
    file_bytes = file_res.content

    # Delete original image out of incoming directory box queue channel
    headers_api = {"Authorization": f"Bearer {DROPBOX_TOKEN}", "Content-Type": "application/json"}
    requests.post("https://api.dropboxapi.com/2/files/delete_v2", headers=headers_api, json={"path": dropbox_path})
    return file_bytes

def upload_vllm_response_to_mobile(json_text_data, output_filename):
    print(f"Pushing feedback loop results tracking packet: {output_filename} back to mobile node...")
    url = "https://content.dropboxapi.com/2/files/upload"
    headers = {
        "Authorization": f"Bearer {DROPBOX_TOKEN}",
        "Content-Type": "application/octet-stream",
        "Dropbox-API-Arg": json.dumps({
            "path": f"/field_outgoing/{output_filename}",
            "mode": "add", "autorename": True, "mute": False
        })
    }
    res = requests.post(url, headers=headers, data=json_text_data.encode('utf-8'))
    if res.status_code != 200:
        print(f"Failed to deposit mobile feedback trace packet: {res.text}")

def run_local_vllm_inference(image_bytes, profile_type):
    base64_str = base64.b64encode(image_bytes).decode('utf-8')
    data_url = f"data:image/jpeg;base64,{base64_str}"
    system_prompt = PROFILE_PROMPTS.get(profile_type, PROFILE_PROMPTS["gauge"])
    
    payload = {
        "model": "loaded-model",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": [
                {"type": "text", "text": "Extract metrics into requested schema profile format. Return clean valid JSON text only."},
                {"type": "image_url", "image_url": {"url": data_url}}
            ]}
        ],
        "temperature": 0.0
    }
    res = requests.post(LM_STUDIO_URL, json=payload)
    res.raise_for_status()
    raw_text = res.json()['choices'][0]['message']['content']
    return raw_text.replace("```json", "").replace("```", "").strip()

def route_engineering_report(json_payload, image_bytes, filename):
    print(f"Dispatching authenticated alert log report out to {TARGET_EMAIL}...")
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = TARGET_EMAIL
    msg['Subject'] = f"Automated Field Intelligence Report - {filename}"

    msg.attach(MIMEText(f"Processed Machine Analytics Struct:\n\n{json_payload}", 'plain'))
    msg.attach(MIMEImage(image_bytes, name=filename))

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, TARGET_EMAIL, msg.as_string())

def execute_polling_loop():
    print("Cloud Feedback Orchestration Engine Online.")
    print("Polling Dropbox root directory structure maps (10s clock intervals)...")
    
    while True:
        try:
            entries = list_dropbox_queue()
            for entry in entries:
                if entry['.tag'] == 'file':
                    dbx_path = entry['path_lower']
                    filename = entry['name']
                    print(f"Asset discovered in pipeline: {filename}")
                    
                    profile_type = "gauge"
                    if "__" in filename:
                        profile_type = filename.split("__")[0]

                    # 1. Fetch data trace, purge incoming cloud queue slot
                    img_bytes = download_and_purge_cloud_file(dbx_path)
                    
                    # 2. Compute visual extraction pass locally on laptop GPU
                    parsed_json_str = run_local_vllm_inference(img_bytes, profile_type)
                    print("Local VLLM evaluation matrix sequence completed cleanly.")
                    
                    # 3. Route engineering email report out via SMTP server channel
                    try:
                        route_engineering_report(parsed_json_str, img_bytes, filename)
                        print("SMTP outbox email synchronization logged successfully.")
                    except Exception as email_error:
                        print(f"Email routing step bypassed due to server error: {email_error}")

                    # 4. Generate return JSON output package filename footprint
                    response_json_name = filename.replace(".jpg", ".json").replace(".jpeg", ".json")
                    
                    # 5. Push results back up to Dropbox cloud paths for phone client ingestion
                    upload_vllm_response_to_mobile(parsed_json_str, response_json_name)
                    print("Feedback pass successfully completed.\n")
                    
        except Exception as e:
            print(f"Pipeline automation execution tracking cycle fault: {e}")
            
        time.sleep(10)

if __name__ == "__main__":
    execute_polling_loop()