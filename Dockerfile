# Start from official miniconda image
FROM continuumio/miniconda3
EXPOSE 8501
# This will be our base folder in image where we'll put src and environment.yml
WORKDIR /code

# Copy environment.yml
COPY ./environment.yml /code/environment.yml

# Install all dependencies
RUN conda env create -f environment.yml


# Activate conda environment/Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "all_nlp_app", "/bin/bash", "-c"]

# Copy source code and config
COPY ./src /code/src
COPY ./config /code/config
COPY ./main.py /code/

# Entrypoint for main script
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "all_nlp_app","streamlit", "run", "main_streamlit.py", "--server.port=8501", "--server.address=0.0.0.0"]