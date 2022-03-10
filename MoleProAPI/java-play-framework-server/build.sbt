name := """molecular-data-provider"""

version := "2.4.1"

lazy val root = (project in file(".")).enablePlugins(PlayJava)

scalaVersion := "2.12.6"

libraryDependencies += "org.webjars" % "swagger-ui" % "3.32.5"
libraryDependencies += "javax.validation" % "validation-api" % "2.0.1.Final"
libraryDependencies += "javax.annotation" % "javax.annotation-api" % "1.3.2"
libraryDependencies += guice
libraryDependencies += filters

scalacOptions in (Compile, doc) += "-no-java-comments"