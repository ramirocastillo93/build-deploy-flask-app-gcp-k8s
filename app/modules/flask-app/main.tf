resource "helm_release" "flask-api" {
  name       = "flask-api-helm"
  repository = "file://./helm"
  chart      = "./helm"

  values = [
    "${file("./helm/values/${var.env}.yaml")}"
  ]
}