# PGSQL DEV
# Chart documentation: https://artifacthub.io/packages/helm/bitnami/postgresql
resource "helm_release" "postgresql_dev" {
  count      = var.env == "prod" ? 0 : 1
  name       = "bitnami"
  repository = "https://charts.bitnami.com/bitnami"
  chart      = "postgresql"

  values = [
    "${file("${path.module}/values.yaml")}"
  ]

  set_sensitive {
    name  = "global.postgresql.auth.postgresPassword"
    value = var.pgPass
  }
  set_sensitive {
    name  = "global.postgresql.auth.username"
    value = var.pgUser
  }
  set_sensitive {
    name  = "global.postgresql.auth.password"
    value = var.pgPass
  }
  set_sensitive {
    name  = "global.postgresql.auth.database"
    value = var.pgDb
  }
}

// PGSQL PROD
resource "helm_release" "postgresql_prod" {
  count      = var.env == "prod" ? 1 : 0
  name       = "bitnami"
  repository = "https://charts.bitnami.com/bitnami"
  chart      = "postgresql-ha"

  set_sensitive {
    name  = "global.postgresql.auth.postgresPassword"
    value = var.pgPass
  }
  set_sensitive {
    name  = "global.postgresql.auth.username"
    value = var.pgUser
  }
  set_sensitive {
    name  = "global.postgresql.auth.password"
    value = var.pgPass
  }
  set_sensitive {
    name  = "global.postgresql.auth.database"
    value = var.pgDb
  }
}