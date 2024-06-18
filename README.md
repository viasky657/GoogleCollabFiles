Ada AI is capable of accepting user input and storing token memory using Zep Memory. The AI can create images for the user by interfacing with the Stable Diffusion Cascade API. In addition, Ada can interface with the Google Serper API as an AI agent and allow it to search the internet for answers to questions. The goal was to create all of these functions with the least amount of memory requirements. Ada was also trained on TensorRT-LLM to speed up its processing time. Ada can also respond to the user with an elevenlabs voice if the user chooses this option. 
Here is the steps of how to set-up this file to run:

####################################################
Step 1: Download the FinalAda.ipynb file. 
##############################################################################
Step 2: Use Google Collab environment and this will work only with a GPU (Preferably the A100 one)
###########################################################################################
Step 3: Run the LLM - RT Set - Up
####################################################################
Step 4: Install TensorRT-LLM for x86_64 users for Mixtral AI and Install for Distilled Whisper Build AI.
#############################################################################################################
Step 5: Install and import libraries for Mixtral AI and for All AI Files
############################################################################################################################
Step 6: Run the Model - Distilled Whisper, Gradio Stable Diffusion Cascade, and Voice AI for Ada including Model Running and Token saving (Short Term Memory and Long Term Memory with Zep). This Model Requires a A100 GPU to run at its most Optimal but other GPUs should work as well; the code execution just may not be as fast.
#################################################################
Step 7 (Alt.): If the Google environment does not support mic access, then run the last code block to run just the Mixtral model without it.
##############################################################################
Note: You will need an Elevenlabs API Key to access the Elevenlabs AI voice option. 
