resource "helm_release" "flask-api" {
  name       = "flask-api-helm_${var.env}"
  repository = "file://./helm"
  chart      = "./helm"
}