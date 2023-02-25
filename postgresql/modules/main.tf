// PGSQL DEV
resource "helm_release" "postgresql_dev" {
  count      = var.env == "prod" ? 0 : 1
  name       = "bitnami"
  repository = "https://charts.bitnami.com/bitnami"
  chart      = "postgresql"

  set_sensitive {
    name  = "global.postgresql.postgresqlPassword"
    value = var.pgPass
  }

  set_sensitive {
    name  = "global.postgresql.postgresqlUsername"
    value = var.pgUser
  }

  set_sensitive {
    name  = "global.postgresql.postgresqlDatabase"
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
    name  = "global.postgresql.password"
    value = var.pgPass
  }

  set_sensitive {
    name  = "global.postgresql.username"
    value = var.pgUser
  }

  set_sensitive {
    name  = "global.postgresql.database"
    value = var.pgDb
  }
}