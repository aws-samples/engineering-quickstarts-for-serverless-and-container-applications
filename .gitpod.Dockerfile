FROM gitpod/workspace-full
RUN sudo apt -y update && sudo apt -y install build-essential git net-tools byobu && \
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
unzip awscliv2.zip && \
sudo ./aws/install && \
ARCH=amd64 && \
PLATFORM=$(uname -s)_$ARCH && \
curl -sLO "https://github.com/eksctl-io/eksctl/releases/latest/download/eksctl_$PLATFORM.tar.gz" && \
tar -xzf eksctl_$PLATFORM.tar.gz -C /tmp && rm eksctl_$PLATFORM.tar.gz && \
sudo mv /tmp/eksctl /usr/local/bin && \
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | sudo bash && \
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl && \
NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && \
brew install derailed/k9s/k9s

# Install Serverless CLI
RUN nvm install --latest; exit 0
RUN npm -i g serverless