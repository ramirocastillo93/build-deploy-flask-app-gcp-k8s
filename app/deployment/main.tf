resource "helm_release" "flask-api" {
    name = "flask-api-helm"
    repository = "file://./helm"
    chart = "./helm"
}