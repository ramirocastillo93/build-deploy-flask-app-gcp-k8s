resource "kubernetes_secret" "gcr-json-key" {
  metadata {
    name = var.k8s_secret_name
  }

  data = {
    ".dockerconfigjson" = jsonencode({
      auths = {
        "${var.k8s_secret_server}" = {
          auth = base64encode("${var.k8s_secret_username}:${file("${path.module}/${var.k8s_secret_password}")}")
        }
      }
    })
  }

  type = "kubernetes.io/dockerconfigjson"
}